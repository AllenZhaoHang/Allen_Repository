package com.entity.vo;

import com.entity.CheliangxinxiEntity;

import com.baomidou.mybatisplus.annotations.TableName;
import java.util.Date;
import org.springframework.format.annotation.DateTimeFormat;

import com.fasterxml.jackson.annotation.JsonFormat;
import java.io.Serializable;
 

/**
 * 车辆信息
 * 手机端接口返回实体辅助类 
 * （主要作用去除一些不必要的字段）
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public class CheliangxinxiVO  implements Serializable {
	private static final long serialVersionUID = 1L;

	 			
	/**
	 * 品牌
	 */
	
	private String pinpai;
		
	/**
	 * 车牌号
	 */
	
	private String chepaihao;
		
	/**
	 * 使用时长
	 */
	
	private String shiyongshizhang;
		
	/**
	 * 维修信息
	 */
	
	private String weixiuxinxi;
		
	/**
	 * 照片
	 */
	
	private String zhaopian;
				
	
	/**
	 * 设置：品牌
	 */
	 
	public void setPinpai(String pinpai) {
		this.pinpai = pinpai;
	}
	
	/**
	 * 获取：品牌
	 */
	public String getPinpai() {
		return pinpai;
	}
				
	
	/**
	 * 设置：车牌号
	 */
	 
	public void setChepaihao(String chepaihao) {
		this.chepaihao = chepaihao;
	}
	
	/**
	 * 获取：车牌号
	 */
	public String getChepaihao() {
		return chepaihao;
	}
				
	
	/**
	 * 设置：使用时长
	 */
	 
	public void setShiyongshizhang(String shiyongshizhang) {
		this.shiyongshizhang = shiyongshizhang;
	}
	
	/**
	 * 获取：使用时长
	 */
	public String getShiyongshizhang() {
		return shiyongshizhang;
	}
				
	
	/**
	 * 设置：维修信息
	 */
	 
	public void setWeixiuxinxi(String weixiuxinxi) {
		this.weixiuxinxi = weixiuxinxi;
	}
	
	/**
	 * 获取：维修信息
	 */
	public String getWeixiuxinxi() {
		return weixiuxinxi;
	}
				
	
	/**
	 * 设置：照片
	 */
	 
	public void setZhaopian(String zhaopian) {
		this.zhaopian = zhaopian;
	}
	
	/**
	 * 获取：照片
	 */
	public String getZhaopian() {
		return zhaopian;
	}
			
}
