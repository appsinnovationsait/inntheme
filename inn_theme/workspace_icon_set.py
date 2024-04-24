import frappe


# @frappe.whitelist()
# def hello_world():
#     text = "hello"
#     return text


@frappe.whitelist()
def get_workspace_sidebar_items():
    from frappe.desk.desktop import Workspace
    from frappe import _

    """Get list of sidebar items for desk"""
    has_access = "Workspace Manager" in frappe.get_roles()

    # don't get domain restricted pages
    blocked_modules = frappe.get_doc("User", frappe.session.user).get_blocked_modules()
    blocked_modules.append("Dummy Module")

    filters = {
        "restrict_to_domain": ["in", frappe.get_active_domains()],
        "module": ["not in", blocked_modules],
    }

    if has_access:
        filters = []

    # pages sorted based on sequence id
    order_by = "sequence_id asc"
    fields = [
        "name",
        "title",
        "for_user",
        "parent_page",
        "content",
        "public",
        "module",
        "icon",
        "is_hidden",
        "custom_svg",
    ]
    all_pages = frappe.get_all(
        "Workspace",
        fields=fields,
        filters=filters,
        order_by=order_by,
        ignore_permissions=True,
    )
    pages = []
    private_pages = []

    # Filter Page based on Permission
    for page in all_pages:
        try:
            workspace = Workspace(page, True)
            if has_access or workspace.is_permitted():
                if page.public and (has_access or not page.is_hidden):
                    pages.append(page)
                elif page.for_user == frappe.session.user:
                    private_pages.append(page)
                page["label"] = _(page.get("name"))
        except frappe.PermissionError:
            pass
    if private_pages:
        pages.extend(private_pages)

    return {"pages": pages, "has_access": has_access}


@frappe.whitelist()
def update_workspace_images():
    data = [
        {"Sr": 1, "ID": "Settings", "SVG": ""},
        {"Sr": 2, "ID": "Build", "SVG": ""},
        {"Sr": 3, "ID": "Integrations", "SVG": ""},
        {"Sr": 4, "ID": "Retail", "SVG": "/assets/inn_theme/images/retails.svg"},
        {
            "Sr": 5,
            "ID": "ERPNext Settings",
            "SVG": "/assets/inn_theme/images/Setting.svg",
        },
        {
            "Sr": 6,
            "ID": "Salespeople",
            "SVG": "/assets/inn_theme/images/salespeopleandbranches.svg",
        },
        {"Sr": 7, "ID": "Website", "SVG": "/assets/inn_theme/images/website.svg"},
        {
            "Sr": 8,
            "ID": "ERPNext Integrations",
            "SVG": "/assets/inn_theme/images/Integration.svg",
        },
        {
            "Sr": 9,
            "ID": "Customization",
            "SVG": "/assets/inn_theme/images/customization.svg",
        },
        {"Sr": 10, "ID": "Utilities", "SVG": ""},
        {"Sr": 11, "ID": "Users", "SVG": "/assets/inn_theme/images/User.svg"},
        {"Sr": 12, "ID": "Tools", "SVG": "/assets/inn_theme/images/Tools.svg"},
        {"Sr": 13, "ID": "Support", "SVG": "/assets/inn_theme/images/Support.svg"},
        {
            "Sr": 14,
            "ID": "Manufacturing",
            "SVG": "/assets/inn_theme/images/manufacturer.svg",
        },
        {"Sr": 15, "ID": "Quality", "SVG": "/assets/inn_theme/images/Quality.svg"},
        {"Sr": 16, "ID": "Projects", "SVG": "/assets/inn_theme/images/Project.svg"},
        {"Sr": 17, "ID": "Loans", "SVG": "/assets/inn_theme/images/Loan.svg"},
        {"Sr": 18, "ID": "Tax & Benefits", "SVG": ""},
        {"Sr": 19, "ID": "Salary Payout", "SVG": ""},
        {"Sr": 20, "ID": "Payroll", "SVG": "/assets/inn_theme/images/Payroll.svg"},
        {"Sr": 21, "ID": "Performance", "SVG": ""},
        {"Sr": 22, "ID": "Leaves", "SVG": ""},
        {"Sr": 23, "ID": "Recruitment", "SVG": ""},
        {"Sr": 24, "ID": "Expense Claims", "SVG": ""},
        {"Sr": 25, "ID": "Shift & Attendance", "SVG": ""},
        {"Sr": 26, "ID": "Employee Lifecycle", "SVG": ""},
        {"Sr": 27, "ID": "HR", "SVG": "/assets/inn_theme/images/HrWhiteRed.svg"},
        {
            "Sr": 28,
            "ID": "Buying",
            "SVG": "/assets/inn_theme/images/BuyingWhiteRed.svg",
        },
        {"Sr": 29, "ID": "Stock", "SVG": "/assets/inn_theme/images/stock.svg"},
        {
            "Sr": 30,
            "ID": "Selling",
            "SVG": "/assets/inn_theme/images/SalesRedWhite.svg",
        },
        {"Sr": 31, "ID": "CRM", "SVG": "/assets/inn_theme/images/CrmWhiteRed.svg"},
        {
            "Sr": 32,
            "ID": "Expenses",
            "SVG": "/assets/inn_theme/images/ExpensesRedWhite.svg",
        },
        {"Sr": 33, "ID": "Assets", "SVG": "/assets/inn_theme/images/Assets.svg"},
        {
            "Sr": 34,
            "ID": "Accounting",
            "SVG": "/assets/inn_theme/images/AccountingRedWhite.svg",
        },
        {"Sr": 35, "ID": "Home", "SVG": "/assets/inn_theme/images/homepage08b992.svg"},
        {"Sr": 36, "ID": "Accounts", "SVG": ""},
        {"Sr": 37, "ID": "Fixed Assets", "SVG": ""},
        {"Sr": 38, "ID": "Inventory", "SVG": ""},
        {
            "Sr": 39,
            "ID": "Branch Sales",
            "SVG": "/assets/inn_theme/images/BranchDox.svg",
        },
    ]
    for row in data:
        if row.get("ID") and row.get("SVG"):
            if frappe.db.exists("Workspace", row.get("ID")):
                if not row.get("SVG") == "":
                    frappe.db.sql(
                        """update `tabWorkspace` set custom_svg=%s where name=%s""",
                        (row.get("SVG"), row.get("ID")),
                    )
