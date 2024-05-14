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


import com.dao.JiaxiaoxinxiDao;
import com.entity.JiaxiaoxinxiEntity;
import com.service.JiaxiaoxinxiService;
import com.entity.vo.JiaxiaoxinxiVO;
import com.entity.view.JiaxiaoxinxiView;

@Service("jiaxiaoxinxiService")
public class JiaxiaoxinxiServiceImpl extends ServiceImpl<JiaxiaoxinxiDao, JiaxiaoxinxiEntity> implements JiaxiaoxinxiService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<JiaxiaoxinxiEntity> page = this.selectPage(
                new Query<JiaxiaoxinxiEntity>(params).getPage(),
                new EntityWrapper<JiaxiaoxinxiEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<JiaxiaoxinxiEntity> wrapper) {
		  Page<JiaxiaoxinxiView> page =new Query<JiaxiaoxinxiView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<JiaxiaoxinxiVO> selectListVO(Wrapper<JiaxiaoxinxiEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public JiaxiaoxinxiVO selectVO(Wrapper<JiaxiaoxinxiEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<JiaxiaoxinxiView> selectListView(Wrapper<JiaxiaoxinxiEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public JiaxiaoxinxiView selectView(Wrapper<JiaxiaoxinxiEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
