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


import com.dao.ZiyuanbeifenDao;
import com.entity.ZiyuanbeifenEntity;
import com.service.ZiyuanbeifenService;
import com.entity.vo.ZiyuanbeifenVO;
import com.entity.view.ZiyuanbeifenView;

@Service("ziyuanbeifenService")
public class ZiyuanbeifenServiceImpl extends ServiceImpl<ZiyuanbeifenDao, ZiyuanbeifenEntity> implements ZiyuanbeifenService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<ZiyuanbeifenEntity> page = this.selectPage(
                new Query<ZiyuanbeifenEntity>(params).getPage(),
                new EntityWrapper<ZiyuanbeifenEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<ZiyuanbeifenEntity> wrapper) {
		  Page<ZiyuanbeifenView> page =new Query<ZiyuanbeifenView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<ZiyuanbeifenVO> selectListVO(Wrapper<ZiyuanbeifenEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public ZiyuanbeifenVO selectVO(Wrapper<ZiyuanbeifenEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<ZiyuanbeifenView> selectListView(Wrapper<ZiyuanbeifenEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public ZiyuanbeifenView selectView(Wrapper<ZiyuanbeifenEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
