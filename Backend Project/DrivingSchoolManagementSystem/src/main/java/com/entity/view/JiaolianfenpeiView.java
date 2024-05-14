package com.entity.view;

import com.entity.JiaolianfenpeiEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import org.apache.commons.beanutils.BeanUtils;
import java.lang.reflect.InvocationTargetException;

import java.io.Serializable;
 

/**
 * 教练分配
 * 后端返回视图实体辅助类   
 * （通常后端关联的表或者自定义的字段需要返回使用）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
@TableName("jiaolianfenpei")
public class JiaolianfenpeiView  extends JiaolianfenpeiEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	public JiaolianfenpeiView(){
	}
 
 	public JiaolianfenpeiView(JiaolianfenpeiEntity jiaolianfenpeiEntity){
 	try {
			BeanUtils.copyProperties(this, jiaolianfenpeiEntity);
		} catch (IllegalAccessException | InvocationTargetException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 		
	}
}
