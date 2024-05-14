package com.entity.view;

import com.entity.DiscussjiaxiaoxinxiEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import org.apache.commons.beanutils.BeanUtils;
import java.lang.reflect.InvocationTargetException;

import java.io.Serializable;
 

/**
 * 驾校信息评论表
 * 后端返回视图实体辅助类   
 * （通常后端关联的表或者自定义的字段需要返回使用）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
@TableName("discussjiaxiaoxinxi")
public class DiscussjiaxiaoxinxiView  extends DiscussjiaxiaoxinxiEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	public DiscussjiaxiaoxinxiView(){
	}
 
 	public DiscussjiaxiaoxinxiView(DiscussjiaxiaoxinxiEntity discussjiaxiaoxinxiEntity){
 	try {
			BeanUtils.copyProperties(this, discussjiaxiaoxinxiEntity);
		} catch (IllegalAccessException | InvocationTargetException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 		
	}
}
