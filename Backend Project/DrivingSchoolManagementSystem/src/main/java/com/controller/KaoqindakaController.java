package com.controller;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Map;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Date;
import java.util.List;
import javax.servlet.http.HttpServletRequest;

import com.utils.ValidatorUtils;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import com.baomidou.mybatisplus.mapper.EntityWrapper;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.annotation.IgnoreAuth;

import com.entity.KaoqindakaEntity;
import com.entity.view.KaoqindakaView;

import com.service.KaoqindakaService;
import com.service.TokenService;
import com.utils.PageUtils;
import com.utils.R;
import com.utils.MD5Util;
import com.utils.MPUtil;
import com.utils.CommonUtil;
import java.io.IOException;

/**
 * 考勤打卡
 * 后端接口
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
@RestController
@RequestMapping("/kaoqindaka")
public class KaoqindakaController {
    @Autowired
    private KaoqindakaService kaoqindakaService;


    


    /**
     * 后端列表
     */
    @RequestMapping("/page")
    public R page(@RequestParam Map<String, Object> params,KaoqindakaEntity kaoqindaka,
		HttpServletRequest request){
		String tableName = request.getSession().getAttribute("tableName").toString();
		if(tableName.equals("jiaolian")) {
			kaoqindaka.setJiaoliangonghao((String)request.getSession().getAttribute("username"));
		}
        EntityWrapper<KaoqindakaEntity> ew = new EntityWrapper<KaoqindakaEntity>();
		PageUtils page = kaoqindakaService.queryPage(params, MPUtil.sort(MPUtil.between(MPUtil.likeOrEq(ew, kaoqindaka), params), params));

        return R.ok().put("data", page);
    }
    
    /**
     * 前端列表
     */
	@IgnoreAuth
    @RequestMapping("/list")
    public R list(@RequestParam Map<String, Object> params,KaoqindakaEntity kaoqindaka, 
		HttpServletRequest request){
        EntityWrapper<KaoqindakaEntity> ew = new EntityWrapper<KaoqindakaEntity>();
		PageUtils page = kaoqindakaService.queryPage(params, MPUtil.sort(MPUtil.between(MPUtil.likeOrEq(ew, kaoqindaka), params), params));
        return R.ok().put("data", page);
    }

	/**
     * 列表
     */
    @RequestMapping("/lists")
    public R list( KaoqindakaEntity kaoqindaka){
       	EntityWrapper<KaoqindakaEntity> ew = new EntityWrapper<KaoqindakaEntity>();
      	ew.allEq(MPUtil.allEQMapPre( kaoqindaka, "kaoqindaka")); 
        return R.ok().put("data", kaoqindakaService.selectListView(ew));
    }

	 /**
     * 查询
     */
    @RequestMapping("/query")
    public R query(KaoqindakaEntity kaoqindaka){
        EntityWrapper< KaoqindakaEntity> ew = new EntityWrapper< KaoqindakaEntity>();
 		ew.allEq(MPUtil.allEQMapPre( kaoqindaka, "kaoqindaka")); 
		KaoqindakaView kaoqindakaView =  kaoqindakaService.selectView(ew);
		return R.ok("查询考勤打卡成功").put("data", kaoqindakaView);
    }
	
    /**
     * 后端详情
     */
    @RequestMapping("/info/{id}")
    public R info(@PathVariable("id") Long id){
        KaoqindakaEntity kaoqindaka = kaoqindakaService.selectById(id);
        return R.ok().put("data", kaoqindaka);
    }

    /**
     * 前端详情
     */
	@IgnoreAuth
    @RequestMapping("/detail/{id}")
    public R detail(@PathVariable("id") Long id){
        KaoqindakaEntity kaoqindaka = kaoqindakaService.selectById(id);
        return R.ok().put("data", kaoqindaka);
    }
    



    /**
     * 后端保存
     */
    @RequestMapping("/save")
    public R save(@RequestBody KaoqindakaEntity kaoqindaka, HttpServletRequest request){
    	kaoqindaka.setId(new Date().getTime()+new Double(Math.floor(Math.random()*1000)).longValue());
    	//ValidatorUtils.validateEntity(kaoqindaka);
        kaoqindakaService.insert(kaoqindaka);
        return R.ok();
    }
    
    /**
     * 前端保存
     */
    @RequestMapping("/add")
    public R add(@RequestBody KaoqindakaEntity kaoqindaka, HttpServletRequest request){
    	kaoqindaka.setId(new Date().getTime()+new Double(Math.floor(Math.random()*1000)).longValue());
    	//ValidatorUtils.validateEntity(kaoqindaka);
        kaoqindakaService.insert(kaoqindaka);
        return R.ok();
    }

    /**
     * 修改
     */
    @RequestMapping("/update")
    public R update(@RequestBody KaoqindakaEntity kaoqindaka, HttpServletRequest request){
        //ValidatorUtils.validateEntity(kaoqindaka);
        kaoqindakaService.updateById(kaoqindaka);//全部更新
        return R.ok();
    }
    

    /**
     * 删除
     */
    @RequestMapping("/delete")
    public R delete(@RequestBody Long[] ids){
        kaoqindakaService.deleteBatchIds(Arrays.asList(ids));
        return R.ok();
    }
    
    /**
     * 提醒接口
     */
	@RequestMapping("/remind/{columnName}/{type}")
	public R remindCount(@PathVariable("columnName") String columnName, HttpServletRequest request, 
						 @PathVariable("type") String type,@RequestParam Map<String, Object> map) {
		map.put("column", columnName);
		map.put("type", type);
		
		if(type.equals("2")) {
			SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
			Calendar c = Calendar.getInstance();
			Date remindStartDate = null;
			Date remindEndDate = null;
			if(map.get("remindstart")!=null) {
				Integer remindStart = Integer.parseInt(map.get("remindstart").toString());
				c.setTime(new Date()); 
				c.add(Calendar.DAY_OF_MONTH,remindStart);
				remindStartDate = c.getTime();
				map.put("remindstart", sdf.format(remindStartDate));
			}
			if(map.get("remindend")!=null) {
				Integer remindEnd = Integer.parseInt(map.get("remindend").toString());
				c.setTime(new Date());
				c.add(Calendar.DAY_OF_MONTH,remindEnd);
				remindEndDate = c.getTime();
				map.put("remindend", sdf.format(remindEndDate));
			}
		}
		
		Wrapper<KaoqindakaEntity> wrapper = new EntityWrapper<KaoqindakaEntity>();
		if(map.get("remindstart")!=null) {
			wrapper.ge(columnName, map.get("remindstart"));
		}
		if(map.get("remindend")!=null) {
			wrapper.le(columnName, map.get("remindend"));
		}

		String tableName = request.getSession().getAttribute("tableName").toString();
		if(tableName.equals("jiaolian")) {
			wrapper.eq("jiaoliangonghao", (String)request.getSession().getAttribute("username"));
		}

		int count = kaoqindakaService.selectCount(wrapper);
		return R.ok().put("count", count);
	}
	







}
