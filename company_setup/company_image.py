# -*- coding: utf-8 -*-
import openerp
from openerp.osv import osv
from openerp import tools
import os
from openerp.tools import image_resize_image

class res_company(osv.osv):
    _inherit="res.company"
    _name="res.company"
    
    def init(self, cr):
        img=open(os.path.join(os.path.dirname(__file__), 'static', 'src', 'img','logo.png'), 'rb') .read().encode('base64')
        cr.execute('UPDATE res_partner SET image=%s WHERE is_company=TRUE', (img,))
        size = (180, None)
        cr.execute('UPDATE res_company SET logo_web=%s', (image_resize_image(img, size),))