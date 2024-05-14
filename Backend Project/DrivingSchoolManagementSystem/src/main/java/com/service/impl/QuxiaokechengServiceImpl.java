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


import com.dao.QuxiaokechengDao;
import com.entity.QuxiaokechengEntity;
import com.service.QuxiaokechengService;
import com.entity.vo.QuxiaokechengVO;
import com.entity.view.QuxiaokechengView;

@Service("quxiaokechengService")
public class QuxiaokechengServiceImpl extends ServiceImpl<QuxiaokechengDao, QuxiaokechengEntity> implements QuxiaokechengService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<QuxiaokechengEntity> page = this.selectPage(
                new Query<QuxiaokechengEntity>(params).getPage(),
                new EntityWrapper<QuxiaokechengEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<QuxiaokechengEntity> wrapper) {
		  Page<QuxiaokechengView> page =new Query<QuxiaokechengView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<QuxiaokechengVO> selectListVO(Wrapper<QuxiaokechengEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public QuxiaokechengVO selectVO(Wrapper<QuxiaokechengEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<QuxiaokechengView> selectListView(Wrapper<QuxiaokechengEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public QuxiaokechengView selectView(Wrapper<QuxiaokechengEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
