package com.entity.view;

import com.entity.JiaochexinxiEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import org.apache.commons.beanutils.BeanUtils;
import java.lang.reflect.InvocationTargetException;

import java.io.Serializable;
 

/**
 * 缴车信息
 * 后端返回视图实体辅助类   
 * （通常后端关联的表或者自定义的字段需要返回使用）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
@TableName("jiaochexinxi")
public class JiaochexinxiView  extends JiaochexinxiEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	public JiaochexinxiView(){
	}
 
 	public JiaochexinxiView(JiaochexinxiEntity jiaochexinxiEntity){
 	try {
			BeanUtils.copyProperties(this, jiaochexinxiEntity);
		} catch (IllegalAccessException | InvocationTargetException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 		
	}
}
