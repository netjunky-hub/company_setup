# company_setup
Odoo company setup module with optional company customizations.

1.) Replace default logo with your company logo

2.) Populate company info (name, address,zip, city, country...)  with the values from res_company_view.xml file

3.) Install other modules and dependencies from __openerp__.py file

4.) Checks the technical features box for administrator user.

More info on our web site:

<a href="http://netjunky.net/create-setup-module-for-odoo-and-change-company-logo" target="_blank">http://netjunky.net/create-setup-module-for-odoo-and-change-company-logo</a>

# mailing_server

1.) Can configure different mail server for mass mailing

Mass mailing server can be different from default Odoo mail server (for example smtp.mandrillapp.com).
If document model is mail.mass_mailing.contact email is sent through mass mailing server.

2.) Can configure different mail servers per user

User can use own mail server.
Mass mailing server is still used for mass mailing.

3.) Mail server priority

If several mail servers are defined use mail server with higher priority  (lower number = higher priority)<br>


