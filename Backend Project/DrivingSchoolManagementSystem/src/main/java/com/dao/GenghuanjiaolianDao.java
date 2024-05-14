package com.dao;

import com.entity.GenghuanjiaolianEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.GenghuanjiaolianVO;
import com.entity.view.GenghuanjiaolianView;


/**
 * 更换教练
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface GenghuanjiaolianDao extends BaseMapper<GenghuanjiaolianEntity> {
	
	List<GenghuanjiaolianVO> selectListVO(@Param("ew") Wrapper<GenghuanjiaolianEntity> wrapper);
	
	GenghuanjiaolianVO selectVO(@Param("ew") Wrapper<GenghuanjiaolianEntity> wrapper);
	
	List<GenghuanjiaolianView> selectListView(@Param("ew") Wrapper<GenghuanjiaolianEntity> wrapper);

	List<GenghuanjiaolianView> selectListView(Pagination page,@Param("ew") Wrapper<GenghuanjiaolianEntity> wrapper);
	
	GenghuanjiaolianView selectView(@Param("ew") Wrapper<GenghuanjiaolianEntity> wrapper);
	

}
