package com.dao;

import com.entity.YuyueliancheEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.YuyueliancheVO;
import com.entity.view.YuyueliancheView;


/**
 * 预约练车
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface YuyueliancheDao extends BaseMapper<YuyueliancheEntity> {
	
	List<YuyueliancheVO> selectListVO(@Param("ew") Wrapper<YuyueliancheEntity> wrapper);
	
	YuyueliancheVO selectVO(@Param("ew") Wrapper<YuyueliancheEntity> wrapper);
	
	List<YuyueliancheView> selectListView(@Param("ew") Wrapper<YuyueliancheEntity> wrapper);

	List<YuyueliancheView> selectListView(Pagination page,@Param("ew") Wrapper<YuyueliancheEntity> wrapper);
	
	YuyueliancheView selectView(@Param("ew") Wrapper<YuyueliancheEntity> wrapper);
	

}
