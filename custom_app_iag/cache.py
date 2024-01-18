import frappe
import functools
import re
from frappe.email import get_cached_contacts, build_match_conditions, update_contact_cache

def clear_cache(doc=None, method=None):
    for key in frappe.cache().hgetall('contacts'):
        frappe.cache().hdel('contacts', key)

@frappe.whitelist()
def get_contact_list(txt, page_length=20):
    """Returns contacts (from autosuggest)"""

    match_conditions = build_match_conditions("Contact")
    match_conditions = "AND {0}".format(match_conditions) if match_conditions else ""

    out = frappe.db.sql(
        f"""
        SELECT DISTINCT * FROM (
            (SELECT ce.email_id AS value, ce.email_id AS label,
            TRIM(BOTH ' ' FROM CONCAT_WS(' ', c.first_name, IFNULL(c.middle_name, ''), c.last_name)) AS description
            FROM `tabContact` c
            INNER JOIN `tabContact Email` ce ON c.name = ce.parent
            WHERE (c.name LIKE %(txt)s OR ce.email_id LIKE %(txt)s) AND ce.email_id != ''
            )
        UNION
            (SELECT u.email AS value, u.email AS label,
            TRIM(BOTH ' ' FROM CONCAT_WS(' ', u.first_name, IFNULL(u.middle_name, ''), u.last_name)) AS description
            FROM `tabUser` u
            WHERE (u.name LIKE %(txt)s OR u.email LIKE %(txt)s OR u.full_name LIKE %(txt)s OR u.username LIKE %(txt)s) AND u.email != ''
            )
        ) AS combined_results
        ORDER BY value
        LIMIT %(page_length)s
        """,
        {"txt": "%" + txt + "%", "page_length": page_length},
        as_dict=True,
    )

    out = filter(None, out)
    return out


@frappe.whitelist()
def get_custom_contact_list(txt, doctype, name, page_length=20):
    """Return email ids for a multiselect field."""
    max_emails = 150 
    _doctype = frappe.get_doc(doctype, name)
    email_list = get_email_list(_doctype)
    limited_email_list = email_list[:max_emails]

    email_regex = "|".join(re.escape(email) for email in limited_email_list)
    sql_query = f"""
        SELECT DISTINCT ce.email_id AS value, ce.email_id AS label,
        CONCAT(c.first_name, IFNULL(CONCAT(' ', c.last_name), '' )) AS description
        FROM `tabContact` c
        INNER JOIN `tabContact Email` ce ON c.name = ce.parent
        WHERE (c.name LIKE %(txt)s OR ce.email_id LIKE %(txt)s) AND ce.email_id != ''
        AND ce.email_id REGEXP '{email_regex}' 
        LIMIT %(page_length)s
    """
    out = frappe.db.sql(
        sql_query,
        {"txt": f"%{txt}%", "page_length": page_length},
        as_dict=True
    )
    return out


def get_email_list(doc):    
    contact_list = []
    filters = [
        ["Dynamic Link", "link_doctype", "=", doc.doctype],
        ["Dynamic Link", "link_name", "=", doc.name],
        ["Dynamic Link", "parenttype", "=", "Contact"],
    ]
    contact_list = frappe.get_list("Contact", filters=filters, fields=["*"])

    for contact in contact_list:
        contact["email_ids"] = frappe.get_all(
            "Contact Email",
            filters={"parenttype": "Contact", "parent": contact.name, "is_primary": 0},
            fields=["email_id"],
        )

    contact_list = sorted(
        contact_list,
        key=functools.cmp_to_key(
            lambda a, b: (int(a.is_primary_contact - b.is_primary_contact))
            or (1 if a.modified - b.modified else 0)
        ),
        reverse=True,
    )

    unique_email_ids = set()

    for contact in contact_list:
        for email_obj in contact.get('email_ids', []):
            email_id = email_obj.get('email_id')
            if email_id:
                unique_email_ids.add(email_id)
        if contact.get('email_id') and contact.get('email_id') != '':
            unique_email_ids.add(contact.get('email_id'))

    unique_email_ids_list = list(unique_email_ids)

    return unique_email_ids_list 