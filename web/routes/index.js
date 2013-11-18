
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', {user: {name: "sarat", age: 21}});
};

exports.settings = function(req, res){
  res.render('settings');
};

exports.rawfeed = function(req, res){
  res.render('rawfeed');
};

exports.partials = function (req, res) {
  var name = req.params.name;
  res.render('partials/' + name);
};
