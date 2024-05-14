package com.entity;

import com.baomidou.mybatisplus.annotations.TableId;
import com.baomidou.mybatisplus.annotations.TableName;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import java.lang.reflect.InvocationTargetException;

import java.io.Serializable;
import java.util.Date;
import java.util.List;

import org.springframework.format.annotation.DateTimeFormat;
import com.fasterxml.jackson.annotation.JsonFormat;
import org.apache.commons.beanutils.BeanUtils;
import com.baomidou.mybatisplus.annotations.TableField;
import com.baomidou.mybatisplus.enums.FieldFill;
import com.baomidou.mybatisplus.enums.IdType;


/**
 * 资源备份
 * 数据库通用操作实体类（普通增删改查）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
@TableName("ziyuanbeifen")
public class ZiyuanbeifenEntity<T> implements Serializable {
	private static final long serialVersionUID = 1L;


	public ZiyuanbeifenEntity() {
		
	}
	
	public ZiyuanbeifenEntity(T t) {
		try {
			BeanUtils.copyProperties(this, t);
		} catch (IllegalAccessException | InvocationTargetException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	/**
	 * 主键id
	 */
	@TableId
	private Long id;
	/**
	 * 资源名称
	 */
					
	private String ziyuanmingcheng;
	
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
				
	@JsonFormat(locale="zh", timezone="GMT+8", pattern="yyyy-MM-dd")
	@DateTimeFormat 		
	private Date beifenshijian;
	
	
	@JsonFormat(locale="zh", timezone="GMT+8", pattern="yyyy-MM-dd HH:mm:ss")
	@DateTimeFormat
	private Date addtime;

	public Date getAddtime() {
		return addtime;
	}
	public void setAddtime(Date addtime) {
		this.addtime = addtime;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}
	/**
	 * 设置：资源名称
	 */
	public void setZiyuanmingcheng(String ziyuanmingcheng) {
		this.ziyuanmingcheng = ziyuanmingcheng;
	}
	/**
	 * 获取：资源名称
	 */
	public String getZiyuanmingcheng() {
		return ziyuanmingcheng;
	}
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
