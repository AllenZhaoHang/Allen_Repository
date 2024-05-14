package com.service.impl;

import org.springframework.stereotype.Service;
import java.util.Map;
import java.util.List;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.mapper.EntityWrapper;
import com.baomidou.mybatisplus.plugins.Page;
import com.baomidou.mybatisplus.service.impl.ServiceImpl;
import com.utils.PageUtils;
import com.utils.Query;


import com.dao.YuyueliancheDao;
import com.entity.YuyueliancheEntity;
import com.service.YuyueliancheService;
import com.entity.vo.YuyueliancheVO;
import com.entity.view.YuyueliancheView;

@Service("yuyueliancheService")
public class YuyueliancheServiceImpl extends ServiceImpl<YuyueliancheDao, YuyueliancheEntity> implements YuyueliancheService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<YuyueliancheEntity> page = this.selectPage(
                new Query<YuyueliancheEntity>(params).getPage(),
                new EntityWrapper<YuyueliancheEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<YuyueliancheEntity> wrapper) {
		  Page<YuyueliancheView> page =new Query<YuyueliancheView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<YuyueliancheVO> selectListVO(Wrapper<YuyueliancheEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public YuyueliancheVO selectVO(Wrapper<YuyueliancheEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<YuyueliancheView> selectListView(Wrapper<YuyueliancheEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public YuyueliancheView selectView(Wrapper<YuyueliancheEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
