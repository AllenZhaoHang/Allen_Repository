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

import com.entity.QingjiashenqingEntity;
import com.entity.view.QingjiashenqingView;

import com.service.QingjiashenqingService;
import com.service.TokenService;
import com.utils.PageUtils;
import com.utils.R;
import com.utils.MD5Util;
import com.utils.MPUtil;
import com.utils.CommonUtil;
import java.io.IOException;

/**
 * 请假申请
 * 后端接口
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
@RestController
@RequestMapping("/qingjiashenqing")
public class QingjiashenqingController {
    @Autowired
    private QingjiashenqingService qingjiashenqingService;


    


    /**
     * 后端列表
     */
    @RequestMapping("/page")
    public R page(@RequestParam Map<String, Object> params,QingjiashenqingEntity qingjiashenqing,
		HttpServletRequest request){
		String tableName = request.getSession().getAttribute("tableName").toString();
		if(tableName.equals("jiaolian")) {
			qingjiashenqing.setJiaoliangonghao((String)request.getSession().getAttribute("username"));
		}
        EntityWrapper<QingjiashenqingEntity> ew = new EntityWrapper<QingjiashenqingEntity>();
		PageUtils page = qingjiashenqingService.queryPage(params, MPUtil.sort(MPUtil.between(MPUtil.likeOrEq(ew, qingjiashenqing), params), params));

        return R.ok().put("data", page);
    }
    
    /**
     * 前端列表
     */
	@IgnoreAuth
    @RequestMapping("/list")
    public R list(@RequestParam Map<String, Object> params,QingjiashenqingEntity qingjiashenqing, 
		HttpServletRequest request){
        EntityWrapper<QingjiashenqingEntity> ew = new EntityWrapper<QingjiashenqingEntity>();
		PageUtils page = qingjiashenqingService.queryPage(params, MPUtil.sort(MPUtil.between(MPUtil.likeOrEq(ew, qingjiashenqing), params), params));
        return R.ok().put("data", page);
    }

	/**
     * 列表
     */
    @RequestMapping("/lists")
    public R list( QingjiashenqingEntity qingjiashenqing){
       	EntityWrapper<QingjiashenqingEntity> ew = new EntityWrapper<QingjiashenqingEntity>();
      	ew.allEq(MPUtil.allEQMapPre( qingjiashenqing, "qingjiashenqing")); 
        return R.ok().put("data", qingjiashenqingService.selectListView(ew));
    }

	 /**
     * 查询
     */
    @RequestMapping("/query")
    public R query(QingjiashenqingEntity qingjiashenqing){
        EntityWrapper< QingjiashenqingEntity> ew = new EntityWrapper< QingjiashenqingEntity>();
 		ew.allEq(MPUtil.allEQMapPre( qingjiashenqing, "qingjiashenqing")); 
		QingjiashenqingView qingjiashenqingView =  qingjiashenqingService.selectView(ew);
		return R.ok("查询请假申请成功").put("data", qingjiashenqingView);
    }
	
    /**
     * 后端详情
     */
    @RequestMapping("/info/{id}")
    public R info(@PathVariable("id") Long id){
        QingjiashenqingEntity qingjiashenqing = qingjiashenqingService.selectById(id);
        return R.ok().put("data", qingjiashenqing);
    }

    /**
     * 前端详情
     */
	@IgnoreAuth
    @RequestMapping("/detail/{id}")
    public R detail(@PathVariable("id") Long id){
        QingjiashenqingEntity qingjiashenqing = qingjiashenqingService.selectById(id);
        return R.ok().put("data", qingjiashenqing);
    }
    



    /**
     * 后端保存
     */
    @RequestMapping("/save")
    public R save(@RequestBody QingjiashenqingEntity qingjiashenqing, HttpServletRequest request){
    	qingjiashenqing.setId(new Date().getTime()+new Double(Math.floor(Math.random()*1000)).longValue());
    	//ValidatorUtils.validateEntity(qingjiashenqing);
        qingjiashenqingService.insert(qingjiashenqing);
        return R.ok();
    }
    
    /**
     * 前端保存
     */
    @RequestMapping("/add")
    public R add(@RequestBody QingjiashenqingEntity qingjiashenqing, HttpServletRequest request){
    	qingjiashenqing.setId(new Date().getTime()+new Double(Math.floor(Math.random()*1000)).longValue());
    	//ValidatorUtils.validateEntity(qingjiashenqing);
        qingjiashenqingService.insert(qingjiashenqing);
        return R.ok();
    }

    /**
     * 修改
     */
    @RequestMapping("/update")
    public R update(@RequestBody QingjiashenqingEntity qingjiashenqing, HttpServletRequest request){
        //ValidatorUtils.validateEntity(qingjiashenqing);
        qingjiashenqingService.updateById(qingjiashenqing);//全部更新
        return R.ok();
    }
    

    /**
     * 删除
     */
    @RequestMapping("/delete")
    public R delete(@RequestBody Long[] ids){
        qingjiashenqingService.deleteBatchIds(Arrays.asList(ids));
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
		
		Wrapper<QingjiashenqingEntity> wrapper = new EntityWrapper<QingjiashenqingEntity>();
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

		int count = qingjiashenqingService.selectCount(wrapper);
		return R.ok().put("count", count);
	}
	







}
