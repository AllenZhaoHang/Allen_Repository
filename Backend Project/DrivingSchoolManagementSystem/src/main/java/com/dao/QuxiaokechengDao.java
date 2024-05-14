package com.dao;

import com.entity.QuxiaokechengEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.QuxiaokechengVO;
import com.entity.view.QuxiaokechengView;


/**
 * 取消课程
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface QuxiaokechengDao extends BaseMapper<QuxiaokechengEntity> {
	
	List<QuxiaokechengVO> selectListVO(@Param("ew") Wrapper<QuxiaokechengEntity> wrapper);
	
	QuxiaokechengVO selectVO(@Param("ew") Wrapper<QuxiaokechengEntity> wrapper);
	
	List<QuxiaokechengView> selectListView(@Param("ew") Wrapper<QuxiaokechengEntity> wrapper);

	List<QuxiaokechengView> selectListView(Pagination page,@Param("ew") Wrapper<QuxiaokechengEntity> wrapper);
	
	QuxiaokechengView selectView(@Param("ew") Wrapper<QuxiaokechengEntity> wrapper);
	

}
