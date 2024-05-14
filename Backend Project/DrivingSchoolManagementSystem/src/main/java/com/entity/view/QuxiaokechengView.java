package com.entity.view;

import com.entity.QuxiaokechengEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import org.apache.commons.beanutils.BeanUtils;
import java.lang.reflect.InvocationTargetException;

import java.io.Serializable;
 

/**
 * 取消课程
 * 后端返回视图实体辅助类   
 * （通常后端关联的表或者自定义的字段需要返回使用）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
@TableName("quxiaokecheng")
public class QuxiaokechengView  extends QuxiaokechengEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	public QuxiaokechengView(){
	}
 
 	public QuxiaokechengView(QuxiaokechengEntity quxiaokechengEntity){
 	try {
			BeanUtils.copyProperties(this, quxiaokechengEntity);
		} catch (IllegalAccessException | InvocationTargetException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 		
	}
}
