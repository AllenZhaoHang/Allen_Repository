package com.entity.model;

import com.entity.ZiyuanbeifenEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import java.util.Date;
import org.springframework.format.annotation.DateTimeFormat;

import com.fasterxml.jackson.annotation.JsonFormat;
import java.io.Serializable;
 

/**
 * 资源备份
 * 接收传参的实体类  
 *（实际开发中配合移动端接口开发手动去掉些没用的字段， 后端一般用entity就够用了） 
 * 取自ModelAndView 的model名称
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public class ZiyuanbeifenModel  implements Serializable {
	private static final long serialVersionUID = 1L;

	 			
	/**
	 * 资源类型
	 */
	
	private String ziyuanleixing;
		
	/**
	 * 资源文件
	 */
	
	private String ziyuanwenjian;
		
	/**
	 * 资源简介
	 */
	
	private String ziyuanjianjie;
		
	/**
	 * 备份时间
	 */
		
	@JsonFormat(locale="zh", timezone="GMT+8", pattern="yyyy-MM-dd HH:mm:ss")
	@DateTimeFormat 
	private Date beifenshijian;
				
	
	/**
	 * 设置：资源类型
	 */
	 
	public void setZiyuanleixing(String ziyuanleixing) {
		this.ziyuanleixing = ziyuanleixing;
	}
	
	/**
	 * 获取：资源类型
	 */
	public String getZiyuanleixing() {
		return ziyuanleixing;
	}
				
	
	/**
	 * 设置：资源文件
	 */
	 
	public void setZiyuanwenjian(String ziyuanwenjian) {
		this.ziyuanwenjian = ziyuanwenjian;
	}
	
	/**
	 * 获取：资源文件
	 */
	public String getZiyuanwenjian() {
		return ziyuanwenjian;
	}
				
	
	/**
	 * 设置：资源简介
	 */
	 
	public void setZiyuanjianjie(String ziyuanjianjie) {
		this.ziyuanjianjie = ziyuanjianjie;
	}
	
	/**
	 * 获取：资源简介
	 */
	public String getZiyuanjianjie() {
		return ziyuanjianjie;
	}
				
	
	/**
	 * 设置：备份时间
	 */
	 
	public void setBeifenshijian(Date beifenshijian) {
		this.beifenshijian = beifenshijian;
	}
	
	/**
	 * 获取：备份时间
	 */
	public Date getBeifenshijian() {
		return beifenshijian;
	}
			
}
