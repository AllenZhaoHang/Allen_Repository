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


import com.dao.JiaolianfenpeiDao;
import com.entity.JiaolianfenpeiEntity;
import com.service.JiaolianfenpeiService;
import com.entity.vo.JiaolianfenpeiVO;
import com.entity.view.JiaolianfenpeiView;

@Service("jiaolianfenpeiService")
public class JiaolianfenpeiServiceImpl extends ServiceImpl<JiaolianfenpeiDao, JiaolianfenpeiEntity> implements JiaolianfenpeiService {
	
	
    @Override
    public PageUtils queryPage(Map<String, Object> params) {
        Page<JiaolianfenpeiEntity> page = this.selectPage(
                new Query<JiaolianfenpeiEntity>(params).getPage(),
                new EntityWrapper<JiaolianfenpeiEntity>()
        );
        return new PageUtils(page);
    }
    
    @Override
	public PageUtils queryPage(Map<String, Object> params, Wrapper<JiaolianfenpeiEntity> wrapper) {
		  Page<JiaolianfenpeiView> page =new Query<JiaolianfenpeiView>(params).getPage();
	        page.setRecords(baseMapper.selectListView(page,wrapper));
	    	PageUtils pageUtil = new PageUtils(page);
	    	return pageUtil;
 	}
    
    @Override
	public List<JiaolianfenpeiVO> selectListVO(Wrapper<JiaolianfenpeiEntity> wrapper) {
 		return baseMapper.selectListVO(wrapper);
	}
	
	@Override
	public JiaolianfenpeiVO selectVO(Wrapper<JiaolianfenpeiEntity> wrapper) {
 		return baseMapper.selectVO(wrapper);
	}
	
	@Override
	public List<JiaolianfenpeiView> selectListView(Wrapper<JiaolianfenpeiEntity> wrapper) {
		return baseMapper.selectListView(wrapper);
	}

	@Override
	public JiaolianfenpeiView selectView(Wrapper<JiaolianfenpeiEntity> wrapper) {
		return baseMapper.selectView(wrapper);
	}


}
