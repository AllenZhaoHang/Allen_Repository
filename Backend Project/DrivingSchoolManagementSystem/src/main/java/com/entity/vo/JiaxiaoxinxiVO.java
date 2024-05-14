package com.entity.vo;

import com.entity.JiaxiaoxinxiEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import java.util.Date;
import org.springframework.format.annotation.DateTimeFormat;

import com.fasterxml.jackson.annotation.JsonFormat;
import java.io.Serializable;
 

/**
 * 驾校信息
 * 手机端接口返回实体辅助类 
 * （主要作用去除一些不必要的字段）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public class JiaxiaoxinxiVO  implements Serializable {
	private static final long serialVersionUID = 1L;

	 			
	/**
	 * 驾校类型
	 */
	
	private String jiaxiaoleixing;
		
	/**
	 * 驾校地址
	 */
	
	private String jiaxiaodizhi;
		
	/**
	 * 报名费用
	 */
	
	private Float baomingfeiyong;
		
	/**
	 * 驾校介绍
	 */
	
	private String jiaxiaojieshao;
		
	/**
	 * 驾校电话
	 */
	
	private String jiaxiaodianhua;
		
	/**
	 * 驾校图片
	 */
	
	private String jiaxiaotupian;
		
	/**
	 * 赞
	 */
	
	private Integer thumbsupnum;
		
	/**
	 * 踩
	 */
	
	private Integer crazilynum;
		
	/**
	 * 最近点击时间
	 */
		
	@JsonFormat(locale="zh", timezone="GMT+8", pattern="yyyy-MM-dd HH:mm:ss")
	@DateTimeFormat 
	private Date clicktime;
		
	/**
	 * 点击次数
	 */
	
	private Integer clicknum;
				
	
	/**
	 * 设置：驾校类型
	 */
	 
	public void setJiaxiaoleixing(String jiaxiaoleixing) {
		this.jiaxiaoleixing = jiaxiaoleixing;
	}
	
	/**
	 * 获取：驾校类型
	 */
	public String getJiaxiaoleixing() {
		return jiaxiaoleixing;
	}
				
	
	/**
	 * 设置：驾校地址
	 */
	 
	public void setJiaxiaodizhi(String jiaxiaodizhi) {
		this.jiaxiaodizhi = jiaxiaodizhi;
	}
	
	/**
	 * 获取：驾校地址
	 */
	public String getJiaxiaodizhi() {
		return jiaxiaodizhi;
	}
				
	
	/**
	 * 设置：报名费用
	 */
	 
	public void setBaomingfeiyong(Float baomingfeiyong) {
		this.baomingfeiyong = baomingfeiyong;
	}
	
	/**
	 * 获取：报名费用
	 */
	public Float getBaomingfeiyong() {
		return baomingfeiyong;
	}
				
	
	/**
	 * 设置：驾校介绍
	 */
	 
	public void setJiaxiaojieshao(String jiaxiaojieshao) {
		this.jiaxiaojieshao = jiaxiaojieshao;
	}
	
	/**
	 * 获取：驾校介绍
	 */
	public String getJiaxiaojieshao() {
		return jiaxiaojieshao;
	}
				
	
	/**
	 * 设置：驾校电话
	 */
	 
	public void setJiaxiaodianhua(String jiaxiaodianhua) {
		this.jiaxiaodianhua = jiaxiaodianhua;
	}
	
	/**
	 * 获取：驾校电话
	 */
	public String getJiaxiaodianhua() {
		return jiaxiaodianhua;
	}
				
	
	/**
	 * 设置：驾校图片
	 */
	 
	public void setJiaxiaotupian(String jiaxiaotupian) {
		this.jiaxiaotupian = jiaxiaotupian;
	}
	
	/**
	 * 获取：驾校图片
	 */
	public String getJiaxiaotupian() {
		return jiaxiaotupian;
	}
				
	
	/**
	 * 设置：赞
	 */
	 
	public void setThumbsupnum(Integer thumbsupnum) {
		this.thumbsupnum = thumbsupnum;
	}
	
	/**
	 * 获取：赞
	 */
	public Integer getThumbsupnum() {
		return thumbsupnum;
	}
				
	
	/**
	 * 设置：踩
	 */
	 
	public void setCrazilynum(Integer crazilynum) {
		this.crazilynum = crazilynum;
	}
	
	/**
	 * 获取：踩
	 */
	public Integer getCrazilynum() {
		return crazilynum;
	}
				
	
	/**
	 * 设置：最近点击时间
	 */
	 
	public void setClicktime(Date clicktime) {
		this.clicktime = clicktime;
	}
	
	/**
	 * 获取：最近点击时间
	 */
	public Date getClicktime() {
		return clicktime;
	}
				
	
	/**
	 * 设置：点击次数
	 */
	 
	public void setClicknum(Integer clicknum) {
		this.clicknum = clicknum;
	}
	
	/**
	 * 获取：点击次数
	 */
	public Integer getClicknum() {
		return clicknum;
	}
			
}
