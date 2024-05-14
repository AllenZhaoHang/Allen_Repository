package com.entity.view;

import com.entity.CaiwuxinxiEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import org.apache.commons.beanutils.BeanUtils;
import java.lang.reflect.InvocationTargetException;

import java.io.Serializable;
 

/**
 * 财务信息
 * 后端返回视图实体辅助类   
 * （通常后端关联的表或者自定义的字段需要返回使用）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
@TableName("caiwuxinxi")
public class CaiwuxinxiView  extends CaiwuxinxiEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	public CaiwuxinxiView(){
	}
 
 	public CaiwuxinxiView(CaiwuxinxiEntity caiwuxinxiEntity){
 	try {
			BeanUtils.copyProperties(this, caiwuxinxiEntity);
		} catch (IllegalAccessException | InvocationTargetException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 		
	}
}
