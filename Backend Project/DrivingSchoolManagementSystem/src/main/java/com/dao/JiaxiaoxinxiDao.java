package com.dao;

import com.entity.JiaxiaoxinxiEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.JiaxiaoxinxiVO;
import com.entity.view.JiaxiaoxinxiView;


/**
 * 驾校信息
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface JiaxiaoxinxiDao extends BaseMapper<JiaxiaoxinxiEntity> {
	
	List<JiaxiaoxinxiVO> selectListVO(@Param("ew") Wrapper<JiaxiaoxinxiEntity> wrapper);
	
	JiaxiaoxinxiVO selectVO(@Param("ew") Wrapper<JiaxiaoxinxiEntity> wrapper);
	
	List<JiaxiaoxinxiView> selectListView(@Param("ew") Wrapper<JiaxiaoxinxiEntity> wrapper);

	List<JiaxiaoxinxiView> selectListView(Pagination page,@Param("ew") Wrapper<JiaxiaoxinxiEntity> wrapper);
	
	JiaxiaoxinxiView selectView(@Param("ew") Wrapper<JiaxiaoxinxiEntity> wrapper);
	

}
