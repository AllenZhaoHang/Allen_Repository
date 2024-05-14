package com.dao;

import com.entity.ZiyuanbeifenEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.ZiyuanbeifenVO;
import com.entity.view.ZiyuanbeifenView;


/**
 * 资源备份
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public interface ZiyuanbeifenDao extends BaseMapper<ZiyuanbeifenEntity> {
	
	List<ZiyuanbeifenVO> selectListVO(@Param("ew") Wrapper<ZiyuanbeifenEntity> wrapper);
	
	ZiyuanbeifenVO selectVO(@Param("ew") Wrapper<ZiyuanbeifenEntity> wrapper);
	
	List<ZiyuanbeifenView> selectListView(@Param("ew") Wrapper<ZiyuanbeifenEntity> wrapper);

	List<ZiyuanbeifenView> selectListView(Pagination page,@Param("ew") Wrapper<ZiyuanbeifenEntity> wrapper);
	
	ZiyuanbeifenView selectView(@Param("ew") Wrapper<ZiyuanbeifenEntity> wrapper);
	

}
