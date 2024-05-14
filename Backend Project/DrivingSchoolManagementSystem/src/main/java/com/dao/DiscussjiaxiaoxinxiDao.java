package com.dao;

import com.entity.DiscussjiaxiaoxinxiEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.DiscussjiaxiaoxinxiVO;
import com.entity.view.DiscussjiaxiaoxinxiView;


/**
 * 驾校信息评论表
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public interface DiscussjiaxiaoxinxiDao extends BaseMapper<DiscussjiaxiaoxinxiEntity> {
	
	List<DiscussjiaxiaoxinxiVO> selectListVO(@Param("ew") Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
	
	DiscussjiaxiaoxinxiVO selectVO(@Param("ew") Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
	
	List<DiscussjiaxiaoxinxiView> selectListView(@Param("ew") Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);

	List<DiscussjiaxiaoxinxiView> selectListView(Pagination page,@Param("ew") Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
	
	DiscussjiaxiaoxinxiView selectView(@Param("ew") Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
	

}
