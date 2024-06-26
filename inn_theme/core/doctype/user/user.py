import frappe


@frappe.whitelist()
def switch_theme(theme):
	if theme in ["Dark", "Light", "Automatic", "InnTheme", "InnThemeBlue", "InnThemePeach"]:
		frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)