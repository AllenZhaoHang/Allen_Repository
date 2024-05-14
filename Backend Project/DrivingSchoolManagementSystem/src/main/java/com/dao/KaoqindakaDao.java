package com.dao;

import com.entity.KaoqindakaEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.KaoqindakaVO;
import com.entity.view.KaoqindakaView;


/**
 * 考勤打卡
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public interface KaoqindakaDao extends BaseMapper<KaoqindakaEntity> {
	
	List<KaoqindakaVO> selectListVO(@Param("ew") Wrapper<KaoqindakaEntity> wrapper);
	
	KaoqindakaVO selectVO(@Param("ew") Wrapper<KaoqindakaEntity> wrapper);
	
	List<KaoqindakaView> selectListView(@Param("ew") Wrapper<KaoqindakaEntity> wrapper);

	List<KaoqindakaView> selectListView(Pagination page,@Param("ew") Wrapper<KaoqindakaEntity> wrapper);
	
	KaoqindakaView selectView(@Param("ew") Wrapper<KaoqindakaEntity> wrapper);
	

}
