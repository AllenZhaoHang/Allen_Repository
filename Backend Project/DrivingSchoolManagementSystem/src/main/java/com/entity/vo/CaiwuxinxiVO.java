package com.entity.vo;

import com.entity.CaiwuxinxiEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import java.util.Date;
import org.springframework.format.annotation.DateTimeFormat;

import com.fasterxml.jackson.annotation.JsonFormat;
import java.io.Serializable;
 

/**
 * 财务信息
 * 手机端接口返回实体辅助类 
 * （主要作用去除一些不必要的字段）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public class CaiwuxinxiVO  implements Serializable {
	private static final long serialVersionUID = 1L;

	 			
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
		
	@JsonFormat(locale="zh", timezone="GMT+8", pattern="yyyy-MM-dd HH:mm:ss")
	@DateTimeFormat 
	private Date tianjiariqi;
				
	
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
