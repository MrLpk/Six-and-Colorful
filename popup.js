// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

//document.write('gg');
  var xhr = new XMLHttpRequest();
  
  xhr.onreadystatechange = processRequest;
  
  var url = 'http://lpkpytest.sinaapp.com';
  xhr.open('GET', url, true);
  xhr.send();
  
  function processRequest(){
    if (xhr.readyState == 4) {
      if (xhr.status == 0 || xhr.status == 200) {
        var data = xhr.responseText;
		alert('...1');
		alert(data);
		alert('...');
      } else {
        document.write('wrong');
      }
    }
  }
  // Note that any URL fetched here must be matched by a permission in
  // the manifest.json file!
  //var url = 'http://lpkpytest.sinaapp.com/';


