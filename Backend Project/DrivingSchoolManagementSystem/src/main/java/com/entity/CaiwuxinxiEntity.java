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
 * 财务信息
 * 数据库通用操作实体类（普通增删改查）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
@TableName("caiwuxinxi")
public class CaiwuxinxiEntity<T> implements Serializable {
	private static final long serialVersionUID = 1L;


	public CaiwuxinxiEntity() {
		
	}
	
	public CaiwuxinxiEntity(T t) {
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
	 * 账单名称
	 */
					
	private String zhangdanmingcheng;
	
	/**
	 * 账单类型
	 */
					
	private String zhangdanleixing;
	
	/**
	 * 账单金额
	 */
					
	private Float zhangdanjine;
	
	/**
	 * 账单描述
	 */
					
	private String zhangdanmiaoshu;
	
	/**
	 * 添加日期
	 */
				
	@JsonFormat(locale="zh", timezone="GMT+8", pattern="yyyy-MM-dd")
	@DateTimeFormat 		
	private Date tianjiariqi;
	
	
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
	 * 设置：账单名称
	 */
	public void setZhangdanmingcheng(String zhangdanmingcheng) {
		this.zhangdanmingcheng = zhangdanmingcheng;
	}
	/**
	 * 获取：账单名称
	 */
	public String getZhangdanmingcheng() {
		return zhangdanmingcheng;
	}
	/**
	 * 设置：账单类型
	 */
	public void setZhangdanleixing(String zhangdanleixing) {
		this.zhangdanleixing = zhangdanleixing;
	}
	/**
	 * 获取：账单类型
	 */
	public String getZhangdanleixing() {
		return zhangdanleixing;
	}
	/**
	 * 设置：账单金额
	 */
	public void setZhangdanjine(Float zhangdanjine) {
		this.zhangdanjine = zhangdanjine;
	}
	/**
	 * 获取：账单金额
	 */
	public Float getZhangdanjine() {
		return zhangdanjine;
	}
	/**
	 * 设置：账单描述
	 */
	public void setZhangdanmiaoshu(String zhangdanmiaoshu) {
		this.zhangdanmiaoshu = zhangdanmiaoshu;
	}
	/**
	 * 获取：账单描述
	 */
	public String getZhangdanmiaoshu() {
		return zhangdanmiaoshu;
	}
	/**
	 * 设置：添加日期
	 */
	public void setTianjiariqi(Date tianjiariqi) {
		this.tianjiariqi = tianjiariqi;
	}
	/**
	 * 获取：添加日期
	 */
	public Date getTianjiariqi() {
		return tianjiariqi;
	}

}
