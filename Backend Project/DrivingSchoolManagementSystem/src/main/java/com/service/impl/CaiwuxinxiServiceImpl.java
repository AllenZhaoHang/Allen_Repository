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


import com.dao.CaiwuxinxiDao;
import com.entity.CaiwuxinxiEntity;
import com.service.CaiwuxinxiService;
import com.entity.vo.CaiwuxinxiVO;
import com.entity.view.CaiwuxinxiView;

@Service("caiwuxinxiService")
public class CaiwuxinxiServiceImpl extends ServiceImpl<CaiwuxinxiDao, CaiwuxinxiEntity> implements CaiwuxinxiService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<CaiwuxinxiEntity> page = this.selectPage(
                new Query<CaiwuxinxiEntity>(params).getPage(),
                new EntityWrapper<CaiwuxinxiEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<CaiwuxinxiEntity> wrapper) {
		  Page<CaiwuxinxiView> page =new Query<CaiwuxinxiView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<CaiwuxinxiVO> selectListVO(Wrapper<CaiwuxinxiEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public CaiwuxinxiVO selectVO(Wrapper<CaiwuxinxiEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<CaiwuxinxiView> selectListView(Wrapper<CaiwuxinxiEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public CaiwuxinxiView selectView(Wrapper<CaiwuxinxiEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
