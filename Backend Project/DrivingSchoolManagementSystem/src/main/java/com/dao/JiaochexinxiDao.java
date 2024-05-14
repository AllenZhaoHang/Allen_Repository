package com.dao;

import com.entity.JiaochexinxiEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.JiaochexinxiVO;
import com.entity.view.JiaochexinxiView;


/**
 * 缴车信息
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public interface JiaochexinxiDao extends BaseMapper<JiaochexinxiEntity> {
	
	List<JiaochexinxiVO> selectListVO(@Param("ew") Wrapper<JiaochexinxiEntity> wrapper);
	
	JiaochexinxiVO selectVO(@Param("ew") Wrapper<JiaochexinxiEntity> wrapper);
	
	List<JiaochexinxiView> selectListView(@Param("ew") Wrapper<JiaochexinxiEntity> wrapper);

	List<JiaochexinxiView> selectListView(Pagination page,@Param("ew") Wrapper<JiaochexinxiEntity> wrapper);
	
	JiaochexinxiView selectView(@Param("ew") Wrapper<JiaochexinxiEntity> wrapper);
	

}
