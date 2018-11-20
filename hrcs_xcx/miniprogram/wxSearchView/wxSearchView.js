/***
 * // 定义数据格式
 * "wxSearchData":{
 *  configconfig:{
 *    style: "wxSearchNormal"
 *  },
 *  view:{
 *    hidden: true,
 *    searchbarHeght: 20
 *  }
 *  hotKeys:[],//自定义热门搜索
 *  his:[]//历史搜索关键字
 *  value
 * }
 */

// 提示集合
var __tipKeys = ['北城', '曹溪', '东城', '东山', '东肖', '莲东', '南城', '西城', '溪南', '邮电', '中城', '北市场', '碧桂园', '地税局', '地质队', '电业局', '东景园', '风动厂', '凤凰城', '凤凰阁', '凤凰隔', '凤凰路', '凤凰苑', '福三线', '富民楼', '干休所', '红炭山', '检查院', '建设局', '交易城', '经贸局', '韭菜园', '矿务局', '乐宜居', '理想城', '莲花山', '林保厂', '林业局', '龙腾路', '绿世界', '米兰阁', '棉纺厂', '民政局', '名都汇', '农业局', '清华园', '水源山', '特钢厂', '天马湾', '天马巷', '外经委', '万和城', '万象城', '万阳城', '微波局', '味精厂', '蜈蚣山', '五交化', '西湖园', '犀牛路', '溪园楼', '新地标', '新发现', '新洲城', '学生街', '羊古墩', '药检所', '医药站', '永龙楼', '邮政局', '御佳园', '裕达园', '裕锦园', '芝华室', '中山街', '中山路', '贮木场', '澳林花园', '宝泰小区', '北城小学', '碧水山庄', '碧水庄园', '滨江花园', '财富旺角', '城市桂冠', '畜牧水产', '党校宿舍', '登高东路', '登高花园', '登高西路', '登高小区', '地质八队', '帝景豪苑', '第一医院', '东湖花园', '东岳花园', '都市新语', '多特家园', '发展大厦', '纺织品站', '凤凰山庄', '凤凰市场', '凤侨新村', '凤小二中', '附小龙高', '附小七中', '附小五中', '富达小区', '富健新村', '富山国际', '富鑫花园', '工行宿舍', '国际山庄', '国贸大厦', '恒宝花园', '恒达工程', '恒大绿洲', '恒生花园', '恒兴嘉苑', '恒兴绿景', '恒亿豪园', '恒亿花园', '红建小区', '红梅小区', '宏泰御景', '宏鑫大厦', '后山电业', '花园广场', '华鼎公馆', '华晖花园', '华侨别墅', '华厦公寓', '华业名都', '皇冠国际', '黄邦雅苑', '汇景大厦', '汇隆小区', '汇盛花园', '汇源大厦', '计委宿舍', '佳宝小区', '家和天下', '嘉华大厦', '嘉华新园', '建材公司', '建材宿舍', '建发上郡', '建发玺院', '建发央郡', '建行宿舍', '建委宿舍', '捷晖小区', '金都锦苑', '金鸡小区', '金鹏花园', '金融中心', '金色家园', '锦绣花园', '锦绣佳园', '景阳小区', '酒厂宿舍', '凯业金爵', '凯业尊爵', '康乐小区', '蓝色港湾', '丽景时代', '利来山庄', '莲东花园', '莲东小区', '莲花大厦', '莲花湖畔', '莲花佳苑', '莲花家园', '莲南小区', '莲西小区', '林景花园', '林隐天下', '龙城春天', '龙初分校', '龙达花园', '龙地华府', '龙地佳苑', '龙钢宿舍', '龙津花园', '龙净环保', '龙马新村', '龙盛花园', '龙腾登高', '龙腾花园', '龙腾星城', '龙铁花苑', '龙铁嘉苑', '龙祥美第', '龙祥小区', '龙兴大厦', '龙岩大道', '龙油锦苑', '龙州时代', '鹭虹花园', '马坑小区', '梅林新村', '美域中央', '美月山庄', '闽西宾馆', '南中旭日', '农机公司', '农资公司', '欧景美月', '欧洲世家', '清华御景', '区国税局', '区粮食局', '燃料公司', '人民银行', '人寿保险', '人造板厂', '融侨观邸', '融侨悦府', '三和大厦', '三和小区', '三建机关', '三建宿舍', '厦鑫花园', '厦鑫瑞锦', '山歌剧团', '山水华庭', '商业车队', '上品至尊', '尚品国际', '晟龙豪庭', '晟龙花园', '盛世家园', '师专宿舍', '石油公司', '实小龙初', '实验二小', '世纪榕华', '市教育局', '市食品厂', '市委宿舍', '水晶嘉园', '水晶中央', '水利水电', '水木莲花', '水韵华都', '松柏花园', '松涛分校', '松涛花园', '松涛龙高', '塔泉大厦', '唐盛花园', '桃源小区', '体育大厦', '体育公园', '体育中心', '天成山庄', '天马明珠', '天马山庄', '天马雅苑', '天宇集团', '天宇宿舍', '天悦莲馨', '条围新村', '挺秀花园', '万宝广场', '万宝名邸', '万成家苑', '万达广场', '万达华城', '万达中心', '旺角一号', '卧龙小区', '五州财富', '五洲财富', '物华花园', '物资大厦', '西安红楼', '西安七中', '西安新村', '西湖人家', '西湖御景', '西山小区', '溪南五中', '香樟名都', '小洋二中', '小洋新城', '谢洋小学', '新惠小区', '新兴大厦', '星辉花园', '兴晖小区', '兴业小区', '学府佳苑', '烟草公司', '盐业公司', '阳光翠庭', '阳光美地', '一中分校', '依云水岸', '亿嘉丽都', '亿兴大厦', '银河大厦', '银河花园', '银河山庄', '雍华名苑', '永丰鑫城', '优山美墅', '油嘴油泵', '御龙首府', '裕福国际', '月山大厦', '月山小区', '造纸新村', '中发荣寓', '中航紫金', '中街龙初', '中骏蓝湾', '珠江花园', '紫金莲园', '紫薇花园', '北城中小学', '碧桂园御府', '材料装饰城', '财校集资房', '电信集资房', '东亚商业城', '都市新天地', '防疫站宿舍', '丰华世纪城', '工商局宿舍', '公安局宿舍', '公路稽征处', '公路局宿舍', '广电局宿舍', '规划局宿舍', '国贸天琴湾', '后门前新村', '华厦名都苑', '教科院附小', '金茂166', '金茂领秀城', '韭菜园党校', '酒厂集资房', '劳动保障局', '莲东保障房', '莲东中小学', '粮食储运站', '龙净生活区', '美伦东锦缘', '闽大集资房', '闽西交易城', '汽车总公司', '侨中念师楼', '轻工局宿舍', '区政府宿舍', '三华乐宜居', '三院集资房', '厦鑫博世园', '晟源家年华', '晟源嘉年华', '市商业车队', '市政府宿舍', '双龙路小区', '双洋新天地', '条围家世界', '万邦棕榈郡', '万盛凤凰城', '卫生防疫站', '阳光城檀悦', '一中教职工', '永兴综合楼', '禹州城上城', '装饰材料城', '北环路安置房', '城市中心花园', '大洋安置小区', '东亚安置小区', '国葳假日花园', '恒宝城市广场', '金茂体育公园', '金茂天马明珠', '劳动服务公司', '莲东恒发电厂', '莲东龙铁名苑', '龙初北城分校', '明珠城市广场', '农业局植保站', '三华城市花园', '糖烟酒集资房', '万宝SOHO', '万达SOHO', '西安安置小区', '西山安置小区', '小洋龙铁名苑', '银河商务宾馆', '纺织品站集资房', '后门前安置小区', '矿泉大厦离休楼', '莲东经济适用房', '莲东新陂安置房', '商业总公司宿舍', '市直机关生活区', '双龙路安置小区', '犀牛路安置小区', '烟厂第一生活区', '紫金山体育公园', '登高西路安置小区', '供销经济贸易公司', '后门前邮政局宿舍', '韭菜园公安局宿舍', '市政维护处安置房', '蜈蚣山市政府宿舍', '犀牛路经济适用房', '犀牛路微利商品房', '水源山李家亭安置小区'];
// 搜索回调函数 
var __searchFunction = null;
// 返回函数 
var __goBackFunction = null;
// 应用变量
var __that = null;

// 初始化函数
function init(that, hotKeys, tipKeys, searchFunction, goBackFunction) {

  __that = that;
  // __tipKeys = tipKeys;
  __searchFunction = searchFunction;
  __goBackFunction = goBackFunction;

  var temData = {};
  var barHeight = 43;
  var view = {
    barHeight: barHeight
  }
  temData.hotKeys = hotKeys;

  wx.getSystemInfo({
    success: function (res) {
      var wHeight = res.windowHeight;
      view.seachHeight = wHeight - barHeight;
      temData.view = view;
      __that.setData({
        wxSearchData: temData
      });
    }
  });

  getHisKeys(__that);
}

// 搜索框输入时候操作
function wxSearchInput(e) {
  var inputValue = e.detail.value;
  // 页面数据
  var temData = __that.data.wxSearchData;
  // 寻找提示值 
  var tipKeys = [];
  if (inputValue && inputValue.length > 0) {
    for (var i = 0; i < __tipKeys.length; i++) {
      var mindKey = __tipKeys[i];
      // 包含字符串
      if (mindKey.indexOf(inputValue) != -1) {
        tipKeys.push(mindKey);
      }
    }
  }
  // 更新数据
  temData.value = inputValue;
  temData.tipKeys = tipKeys;
  // 更新视图
  __that.setData({
    wxSearchData: temData
  });
}

// 清空输入
function wxSearchClear() {
  // 页面数据
  var temData = __that.data.wxSearchData;
  // 更新数据
  temData.value = "";
  temData.tipKeys = [];
  // 更新视图
  __that.setData({
    wxSearchData: temData
  });
}

// 点击提示或者关键字、历史记录时的操作
function wxSearchKeyTap(e) {
  search(e.target.dataset.key);
}

// 确任或者回车
function wxSearchConfirm(e) {
  var key = e.target.dataset.key;
  if(key=='back'){
    __goBackFunction();
  }else{
    search(__that.data.wxSearchData.value);
  }
}

function search(inputValue) {
  if (inputValue && inputValue.length > 0) {
    // 添加历史记录
    //wxSearchAddHisKey(inputValue);
    // 更新
    var temData = __that.data.wxSearchData;
    temData.value = inputValue;
    __that.setData({
      wxSearchData: temData
    });
    // 回调搜索
    __searchFunction(inputValue);
  }
}

// 读取缓存
function getHisKeys() {
  var value = [];
  try {
    value = wx.getStorageSync('wxSearchHisKeys')
    if (value) {
      // Do something with return value
      var temData = __that.data.wxSearchData;
      temData.his = value;
      __that.setData({
        wxSearchData: temData
      });
    }
  } catch (e) {
    // Do something when catch error
  }
}

// 添加缓存
function wxSearchAddHisKey(inputValue) {
  if (!inputValue || inputValue.length == 0) {
    return;
  }
  var value = wx.getStorageSync('wxSearchHisKeys');
  if (value) {
    if (value.indexOf(inputValue) < 0) {
      value.unshift(inputValue);
    }
    wx.setStorage({
      key: "wxSearchHisKeys",
      data: value,
      success: function () {
        getHisKeys(__that);
      }
    })
  } else {
    value = [];
    value.push(inputValue);
    wx.setStorage({
      key: "wxSearchHisKeys",
      data: value,
      success: function () {
        getHisKeys(__that);
      }
    })
  }
}

// 删除缓存
function wxSearchDeleteAll() {
  wx.removeStorage({
    key: 'wxSearchHisKeys',
    success: function (res) {
      var value = [];
      var temData = __that.data.wxSearchData;
      temData.his = value;
      __that.setData({
        wxSearchData: temData
      });
    }
  })
}

// 导出接口
module.exports = {
  init: init, //初始化函数
  wxSearchInput: wxSearchInput,// 输入变化时的操作
  wxSearchKeyTap: wxSearchKeyTap, // 点击提示或者关键字、历史记录时的操作
  wxSearchDeleteAll: wxSearchDeleteAll, // 删除所有的历史记录
  wxSearchConfirm: wxSearchConfirm, // 搜索函数
  wxSearchClear: wxSearchClear,  // 清空函数
}