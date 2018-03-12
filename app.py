#!/usr/bin/env python
#coding:utf-8

import tornado
import tornado.ioloop
import tornado.web
from tornado.options import define,options
import os
from handlers.Handlers import *
from config.settings import websettings
import tornado.httpserver
from app.dbWrapper import dbWrapper

define("port", default=80, help="run on the given port", type=int)

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/',mainHandler),
            (r'/rent/?',rentHandler),
            (r'/host/?',hostHandler),
            (r'/contact/?',contactHandler),
            (r'/slt/?',solutionHandler),
            (r'/visit/?',vistHandler),
            (r'/news/([a-zA-Z0-9\-]*)',newsHandler),
            (r'/as-service/?',asServiceHandler),
            (r'/service-contract/?',serviceContractHandler),
            (r'/activities/?',activitiesHandler),
            (r'/checkcaptcha/?', checkCaptchaHandler),
            (r'/captcha/?', captchaHandler),
            (r'/admin/?',adminLoginHandler),
            (r'/admin/overview/?',adminOverviewHandler),
            (r'/admin/all-machines/?',adminAllMahcinesHandler),
            (r'/admin/machines/?',adminMachinesHandler),
            (r'/admin/add-machines/',adminAddMachinesHandler),
            (r'/admin/machine/release/?',adminMachineReleaseHandler),
            (r'/admin/machine/modify?', adminMachineModifyHandler),
            (r'/admin/machine/checkms/', adminMachineCheckHandler),
            (r'/admin/removems/(\d*)', removeMachineHandler),
            (r'/admin/orders/?',adminOrdersHandler),
            (r'/admin/redirect/?',adminRedirectHandler),
            (r'/admin/add-orders/',adminAddOrderHandler),
            (r'/admin/order/modify/([a-zA-Z0-9\-]*)',adminOrdersModifyHandler),
            (r'/admin/order/renew/?',adminOrderRenewHandler),
            (r'/admin/order/audit/',adminOrderAuditHandler),
            (r'/admin/order/remove/(\d*)', adminOrderRemoveHandler),
            (r'/admin/order/release/',adminOrderReleaseHandler),
            (r'/admin/order/suborder/',adminSuborderHandler),
            (r'/admin/orders/checkip/',adminOrderCheckHandler),

            (r'/admin/publish/?',adminPublishHandler),
            (r'/admin/financial/?', adminFinancialHandler),
            (r'/admin/financial/edit/?', adminFinancialEditHandler),
            (r'/admin/statistics/?', adminStatisticsHandler),
            (r'/admin/clients/?',adminClientsHandler),
            (r'/admin/client/remove/(\d*)', clientRemoveHandler),
            (r'/admin/resetpwd/?', adminResetPwdHandler),
            (r'/admin/client/edit/?', clientModifyHandler),
            (r'/admin/mpwdresult/?',adminModifyPwdRedirectHandler),
            (r'/admin/mpredirect/?',adminMpRedirectHandler),
            (r'/admin/client/bind/',adminClientBindHandler),
            (r'/admin/add/?', adminAddHandler),
            (r'/admin/addredirect/?',adminAddRedirectHandler),
            (r'/admin/addsuccess/?',adminAddSuccessHandler),
            (r'/admin/oexport/',adminOrderExportHandler),
            (r'/client/auth/?', clientAuthHandler),
            (r'/client/checkmsg/(\d*)', clientCheckmsgHandler),
            (r'/client/checkmobile/(\d*)', clientCheckMobileHandler),
            (r'/client/reg/?',clientRegHandler),
            (r'/client/getmsg/?',clientMsgHandler),
            (r'/client/mypanel/',clientPanelHandler),
            (r'/client/redirect/', clientRedirectHandler),
            (r'/client/lgredirect/',clientLgredirectHandler),
            (r'/quit/?', quitHandler),
            (r'/cquit/?', clientQuitHandler),#quite handler for clients
            (r'(.*)', baseHandler)
        ]
        super(Application, self).__init__(handlers,**websettings)
        self.db = dbWrapper()

		
if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
