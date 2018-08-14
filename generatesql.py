#!/usr/bin/env python3


sql='''
drop DATABASE hongbao;
CREATE DATABASE  hongbao CHARACTER SET utf8 ;

USE hongbao;

'''
for i in range(1,257):
    sql += '''
    -- ----------------------------
    -- Table structure for hongbao_%s   
    -- ----------------------------
    CREATE TABLE hongbao_%s (
      `id` bigint(21)  unsigned   NOT NULL AUTO_INCREMENT COMMENT '自增id',
      `hb_id` varchar(50)  NOT NULL COMMENT '红包ID',
      `activity_id` bigint(21)  DEFAULT NULL COMMENT '活动ID',
      `activity_name` varchar(50) DEFAULT NULL COMMENT '活动名称',
      `hb_type` int(11) DEFAULT NULL COMMENT '红包类型 1：普通红包 2：助力红包',
      `begin_time` datetime NOT NULL COMMENT '有效开始时间',
      `end_time` datetime NOT NULL COMMENT '有效结束时间',
      `discount` decimal(10,2)  NOT NULL COMMENT '红包面额',
      `balance` decimal(10,2)  NOT NULL COMMENT '余额',
      `hb_state` tinyint(4) NOT NULL COMMENT '红包的状态 0作废 1未发放 2未使用 3已使用4已过期',
      `channel` varchar(50) NOT NULL COMMENT '红包领取渠道',      
      `use_time` datetime DEFAULT NULL COMMENT '使用时间',
      `pin` varchar(50) DEFAULT NULL COMMENT '用户pin',
      `yn` tinyint(4) NOT NULL COMMENT '是否有效',
      `create_time` datetime NOT NULL COMMENT '创建时间',
      `update_time` datetime NOT NULL COMMENT '修改时间',
      PRIMARY KEY (`id`)
    ) ENGINE=Innodb AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT="红包表";
    ALTER TABLE `hongbao`.`hongbao_%s`  ADD UNIQUE INDEX `unique_hbid_pin_index`(`hb_id`, `pin`);
    ''' % (i,i,i)
    sql+='''
    -- ----------------------------
    -- Table structure for hongbao_detail_%s   
    -- ----------------------------
    CREATE TABLE hongbao_detail_%s (
      `id` bigint(21)  unsigned   NOT NULL AUTO_INCREMENT COMMENT '自增id',
      `hb_id` varchar(50)  NOT NULL COMMENT '红包ID',
      `pin` varchar(50) NOT NULL COMMENT '用户pin',
      `amount` decimal(10,2)  NOT NULL COMMENT '操作涉及的红包金额',
      `operate_type` int(11) NOT NULL COMMENT '操作类型 1领取2使用3回滚',
      `bus_id` varchar(50) DEFAULT NULL COMMENT '业务编号',
      `rftype` varchar(50) DEFAULT NULL COMMENT '发放或者操作业务类型 业务码',
      `remark` varchar(100) DEFAULT NULL COMMENT '备注',
      `ip` varchar(32) DEFAULT NULL COMMENT 'IP',
      `uuid` varchar(100) DEFAULT NULL COMMENT 'uuid',
      `yn` tinyint(4) NOT NULL COMMENT '是否有效',
      `create_time` datetime NOT NULL COMMENT '创建时间',
      `update_time` datetime NOT NULL COMMENT '修改时间',
      PRIMARY KEY (`id`)
    ) ENGINE=Innodb AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT="红包明细表";
    alter table hongbao_detail_%s add unique index uniq_hbid_pin_busId_rftype_operateType_index(hb_id,pin,bus_id,rftype,operate_type);
    ''' %(i,i,i)

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()
save_to_file("sql.text",sql)
print(sql)