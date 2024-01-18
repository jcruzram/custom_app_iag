from . import __version__ as app_version

app_name = "custom_app_iag"
app_title = "Custom App IAG"
app_publisher = "IAG"
app_description = "Customization for IAG."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@ia-group.com.au"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom_app_iag/css/custom_app_iag.css"
app_include_js = ["/assets/custom_app_iag/js/communication_override.js", "/assets/js/custom_app_iag.js"]

# include js, css files in header of web template
# web_include_css = "/assets/custom_app_iag/css/custom_app_iag.css"
# web_include_js = "/assets/custom_app_iag/js/custom_app_iag.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "custom_app_iag/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Communication" : "public/js/communication.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "custom_app_iag.install.before_install"
# after_install = "custom_app_iag.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "custom_app_iag.uninstall.before_uninstall"
# after_uninstall = "custom_app_iag.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_app_iag.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Contact": {
		"on_update": "custom_app_iag.cache.clear_cache",
		"on_cancel": "custom_app_iag.cache.clear_cache",
		"on_trash": "custom_app_iag.cache.clear_cache"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"custom_app_iag.tasks.all"
#	],
#	"daily": [
#		"custom_app_iag.tasks.daily"
#	],
#	"hourly": [
#		"custom_app_iag.tasks.hourly"
#	],
#	"weekly": [
#		"custom_app_iag.tasks.weekly"
#	]
#	"monthly": [
#		"custom_app_iag.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "custom_app_iag.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"frappe.email.get_contact_list": "custom_app_iag.cache.get_contact_list",
    "frappe.desk.form.load.get_docinfo": "custom_app_iag.load.form.get_docinfo",
    "frappe.desk.form.load.getdoc": "custom_app_iag.load.form.getdoc",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "custom_app_iag.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"custom_app_iag.auth.validate"
# ]

