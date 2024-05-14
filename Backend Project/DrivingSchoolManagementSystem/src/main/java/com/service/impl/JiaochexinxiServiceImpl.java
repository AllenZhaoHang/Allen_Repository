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


import com.dao.JiaochexinxiDao;
import com.entity.JiaochexinxiEntity;
import com.service.JiaochexinxiService;
import com.entity.vo.JiaochexinxiVO;
import com.entity.view.JiaochexinxiView;

@Service("jiaochexinxiService")
public class JiaochexinxiServiceImpl extends ServiceImpl<JiaochexinxiDao, JiaochexinxiEntity> implements JiaochexinxiService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<JiaochexinxiEntity> page = this.selectPage(
                new Query<JiaochexinxiEntity>(params).getPage(),
                new EntityWrapper<JiaochexinxiEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<JiaochexinxiEntity> wrapper) {
		  Page<JiaochexinxiView> page =new Query<JiaochexinxiView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<JiaochexinxiVO> selectListVO(Wrapper<JiaochexinxiEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public JiaochexinxiVO selectVO(Wrapper<JiaochexinxiEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<JiaochexinxiView> selectListView(Wrapper<JiaochexinxiEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public JiaochexinxiView selectView(Wrapper<JiaochexinxiEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
