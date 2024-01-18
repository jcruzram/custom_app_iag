class CustomCommunicationComposer extends frappe.views.CommunicationComposer {
	setup_multiselect_queries() {
		const doctypes = ["Customer", "Supplier","User"];
		const fieldsToQuery = ["recipients", "cc", "bcc"];
        const fieldsToApply = ["recipients"]

        let method = "frappe.email.get_contact_list";
		let args = { txt: "" };
		// let _name = "";
		
		fieldsToQuery.forEach((field) => {
			console.log('--------------------------');
			console.log(field);
			console.log(this.doc);
			console.log(this.doc.doctype);
			console.log(doctypes.includes(this.doc.doctype));
			console.log('--------------------------');
            if (this.doc && this.doc.doctype && doctypes.includes(this.doc.doctype)) {
                if(fieldsToApply.includes(field)){
                    method = "custom_app_iag.cache.get_custom_contact_list";
                    args.doctype = this.doc.doctype;
					args.name = this.doc.name;
                }
            }
			this.dialog.fields_dict[field].get_data = () => {
				const data = this.dialog.fields_dict[field].get_value();
				const txt = data.match(/[^,\s*]*$/)[0] || "";
				console.log(method);
				console.log(args);
				frappe.call({
					method: method,
					args: args,
					callback: (r) => {
						this.dialog.fields_dict[field].set_data(r.message);
					},
				});
			};
		});
	}
}

frappe.views.CommunicationComposer = CustomCommunicationComposer;

