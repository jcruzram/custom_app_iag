class CustomCommunicationComposer extends frappe.views.CommunicationComposer {
	setup_multiselect_queries() {
		const doctypes = ["Customer"];
		const fieldsToQuery = ["recipients", "cc", "bcc"];
        const fieldsToApply = ["recipients"]

        let method = "frappe.email.get_contact_list";
		let args = { txt: "" };

		fieldsToQuery.forEach((field) => {

            if (this.doc && this.doc.doctype && doctypes.includes(this.doc.doctype)) {
                if(fieldsToApply.includes(field)){
                    method = "n_gme.cache.get_custom_contact_list";
                    args.name = this.doc.name;
                }
            }
			this.dialog.fields_dict[field].get_data = () => {
				const data = this.dialog.fields_dict[field].get_value();
				const txt = data.match(/[^,\s*]*$/)[0] || "";

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

