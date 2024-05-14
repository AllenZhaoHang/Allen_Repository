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


import com.dao.GenghuanjiaolianDao;
import com.entity.GenghuanjiaolianEntity;
import com.service.GenghuanjiaolianService;
import com.entity.vo.GenghuanjiaolianVO;
import com.entity.view.GenghuanjiaolianView;

@Service("genghuanjiaolianService")
public class GenghuanjiaolianServiceImpl extends ServiceImpl<GenghuanjiaolianDao, GenghuanjiaolianEntity> implements GenghuanjiaolianService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<GenghuanjiaolianEntity> page = this.selectPage(
                new Query<GenghuanjiaolianEntity>(params).getPage(),
                new EntityWrapper<GenghuanjiaolianEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<GenghuanjiaolianEntity> wrapper) {
		  Page<GenghuanjiaolianView> page =new Query<GenghuanjiaolianView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<GenghuanjiaolianVO> selectListVO(Wrapper<GenghuanjiaolianEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public GenghuanjiaolianVO selectVO(Wrapper<GenghuanjiaolianEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<GenghuanjiaolianView> selectListView(Wrapper<GenghuanjiaolianEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public GenghuanjiaolianView selectView(Wrapper<GenghuanjiaolianEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
