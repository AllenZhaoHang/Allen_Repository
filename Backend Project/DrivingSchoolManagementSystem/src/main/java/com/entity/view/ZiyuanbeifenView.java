package com.entity.view;

import com.entity.ZiyuanbeifenEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import org.apache.commons.beanutils.BeanUtils;
import java.lang.reflect.InvocationTargetException;

import java.io.Serializable;
 

/**
 * 资源备份
 * 后端返回视图实体辅助类   
 * （通常后端关联的表或者自定义的字段需要返回使用）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
@TableName("ziyuanbeifen")
public class ZiyuanbeifenView  extends ZiyuanbeifenEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	public ZiyuanbeifenView(){
	}
 
 	public ZiyuanbeifenView(ZiyuanbeifenEntity ziyuanbeifenEntity){
 	try {
			BeanUtils.copyProperties(this, ziyuanbeifenEntity);
		} catch (IllegalAccessException | InvocationTargetException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 		
	}
}
