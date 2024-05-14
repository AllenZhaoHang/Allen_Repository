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


import com.dao.DiscussjiaxiaoxinxiDao;
import com.entity.DiscussjiaxiaoxinxiEntity;
import com.service.DiscussjiaxiaoxinxiService;
import com.entity.vo.DiscussjiaxiaoxinxiVO;
import com.entity.view.DiscussjiaxiaoxinxiView;

@Service("discussjiaxiaoxinxiService")
public class DiscussjiaxiaoxinxiServiceImpl extends ServiceImpl<DiscussjiaxiaoxinxiDao, DiscussjiaxiaoxinxiEntity> implements DiscussjiaxiaoxinxiService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<DiscussjiaxiaoxinxiEntity> page = this.selectPage(
                new Query<DiscussjiaxiaoxinxiEntity>(params).getPage(),
                new EntityWrapper<DiscussjiaxiaoxinxiEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<DiscussjiaxiaoxinxiEntity> wrapper) {
		  Page<DiscussjiaxiaoxinxiView> page =new Query<DiscussjiaxiaoxinxiView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<DiscussjiaxiaoxinxiVO> selectListVO(Wrapper<DiscussjiaxiaoxinxiEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public DiscussjiaxiaoxinxiVO selectVO(Wrapper<DiscussjiaxiaoxinxiEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<DiscussjiaxiaoxinxiView> selectListView(Wrapper<DiscussjiaxiaoxinxiEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public DiscussjiaxiaoxinxiView selectView(Wrapper<DiscussjiaxiaoxinxiEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
