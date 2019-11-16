#: Operation ids
ops = [
    "transfer",
    "limit_order_create",
    "limit_order_cancel",
    "call_order_update",
    "fill_order",
    "account_create",
    "account_update",
    "account_whitelist",
    "account_upgrade",
    "account_transfer",
    "asset_create",
    "asset_update",
    "asset_update_bitasset",
    "asset_update_feed_producers",
    "asset_issue",
    "asset_reserve",
    "asset_fund_fee_pool",
    "asset_settle",
    "asset_global_settle",
    "asset_publish_feed",
    "witness_create",
    "witness_update",
    "proposal_create",
    "proposal_update",
    "proposal_delete",
    "withdraw_permission_create",
    "withdraw_permission_update",
    "withdraw_permission_claim",
    "withdraw_permission_delete",
    "committee_member_create",
    "committee_member_update",
    "committee_member_update_global_parameters",
    "vesting_balance_create",
    "vesting_balance_withdraw",
    "worker_create",
    "custom",
    "assert",
    "balance_claim",
    "override_transfer",
    "transfer_to_blind",
    "blind_transfer",
    "transfer_from_blind",
    "asset_settle_cancel",
    "asset_claim_fees",
    "fba_distribute",
    "bid_collateral",
    "execute_bid",
    # ZOS新加operation
    "account_property",#      //赋权网关或者运营商
    "gateway_withdraw",#      //提币
    "gateway_deposit",#       //充值
    "gateway_issue_currency",# //给网关发行货币
    "bitlender_option_create",#  //创建法币参数
    "bitlender_option_author",#  //创建法币董事会
    "bitlender_option_update",#  //修改法币参数
    "bitlender_rate_update",#      //修改法币率利
    "asset_property",#             //赋权资产为法币或可抵押数字货币
    "bitlender_loan",#             //借款
    "bitlender_invest",#           //投资
    "bitlender_repay_interest",#   //还息
    "bitlender_overdue_interest",# //逾期还利息
    "bitlender_repay_principal",#  //还款
    "bitlender_pre_repay_principal",#       //提前还款            
    "bitlender_overdue_repay_principal",#    //逾期还款
    "bitlender_add_collateral",#   //增加抵押
    "bitlender_recycle",#          //处理不良资产
    "bitlender_autorepayment",#    //自动还款账户
    "fill_object_history",#                  // VIRTUAL       
    "finance_option_create",#  //创建筹资参数            
    "finance_option_update",#  //修改筹资参数     
    "finance_create",#         //筹资 
    "finance_enable",#         //筹资有效             
    "account_coupon",#         //增加优惠卷
    "change_identity",#              //激活见证人
    "bitlender_autorepayment",#      //自动还款
    "withdraw_exchange_fee",#        //提取费用            
    "bitlender_paramers_update",#    //修改借贷系统参数     
    "gateway_create",#
    "gateway_update",#
    "carrier_create",#
    "carrier_update",#
    "budget_member_create",#
    "budget_member_update",#
    "transfer_vesting",#
    "revoke_vesting",#
    "bitlender_remove",#             //取消借款            
    "bitlender_squeeze",#             //VIRTUAL 
    "bitlender_publish_feed",#        //借贷喂价            
    "bitlender_update_feed_producers",# //更新借贷喂价人
    "bitlender_test"#                 //测试，不要使用    gou                                     
]
operations = {o: ops.index(o) for o in ops}


def getOperationNameForId(i):
    """ Convert an operation id into the corresponding string
    """
    for key in operations:
        if int(operations[key]) is int(i):
            return key
    return "Unknown Operation ID %d" % i
