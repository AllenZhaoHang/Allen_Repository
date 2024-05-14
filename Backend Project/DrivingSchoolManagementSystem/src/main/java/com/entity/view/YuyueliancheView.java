package com.entity.view;

import com.entity.YuyueliancheEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import org.apache.commons.beanutils.BeanUtils;
import java.lang.reflect.InvocationTargetException;

import java.io.Serializable;
 

/**
 * 预约练车
 * 后端返回视图实体辅助类   
 * （通常后端关联的表或者自定义的字段需要返回使用）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
@TableName("yuyuelianche")
public class YuyueliancheView  extends YuyueliancheEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	public YuyueliancheView(){
	}
 
 	public YuyueliancheView(YuyueliancheEntity yuyueliancheEntity){
 	try {
			BeanUtils.copyProperties(this, yuyueliancheEntity);
		} catch (IllegalAccessException | InvocationTargetException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 		
	}
}
