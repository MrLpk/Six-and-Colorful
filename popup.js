// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

  var xhr = new XMLHttpRequest();
  
  xhr.onreadystatechange = processRequest;
  
  var url = 'http://sixandcolor.sinaapp.com/check';
  xhr.open('GET', url, true);
  xhr.send();
  
  function processRequest(){
    if (xhr.readyState == 4) {
      if (xhr.status == 0 || xhr.status == 200) {
        var data = xhr.responseText;
        // document.write(data);
        alert(data);
        data = "{"d": [38, 48, 47, 6, 30, 15], "s": "40", "t": "2013/10/29", "n": "125"}";
        var obj = eval('('+data+')');
        alert(obj);
        var div = document.getElementById("d");
        div.innerHTML = obj.n;
      } else {
        document.write('wrong');
      }
    }
  }
  // Note that any URL fetched here must be matched by a permission in
  // the manifest.json file!
  //var url = 'http://lpkpytest.sinaapp.com/';


