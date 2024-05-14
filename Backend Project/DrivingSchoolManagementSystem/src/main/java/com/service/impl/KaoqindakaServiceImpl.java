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


import com.dao.KaoqindakaDao;
import com.entity.KaoqindakaEntity;
import com.service.KaoqindakaService;
import com.entity.vo.KaoqindakaVO;
import com.entity.view.KaoqindakaView;

@Service("kaoqindakaService")
public class KaoqindakaServiceImpl extends ServiceImpl<KaoqindakaDao, KaoqindakaEntity> implements KaoqindakaService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<KaoqindakaEntity> page = this.selectPage(
                new Query<KaoqindakaEntity>(params).getPage(),
                new EntityWrapper<KaoqindakaEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<KaoqindakaEntity> wrapper) {
		  Page<KaoqindakaView> page =new Query<KaoqindakaView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<KaoqindakaVO> selectListVO(Wrapper<KaoqindakaEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public KaoqindakaVO selectVO(Wrapper<KaoqindakaEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<KaoqindakaView> selectListView(Wrapper<KaoqindakaEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public KaoqindakaView selectView(Wrapper<KaoqindakaEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
