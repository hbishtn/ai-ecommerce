(function(){
  function applyColor(hex){
    if(!hex) return;
    document.documentElement.style.setProperty('--brand', hex);
    // derive darker primary for buttons
    document.documentElement.style.setProperty('--primary', hex);
  }

  // load from localStorage
  var saved = localStorage.getItem('themeColor');
  if(saved){ applyColor(saved); }

  // if meta tag present, use it (allows server-side injection)
  var meta = document.querySelector('meta[name="theme-color"]');
  if(meta && meta.content) { applyColor(meta.content); localStorage.setItem('themeColor', meta.content); }

  // UI handlers
  function setupPicker(){
    var picker = document.getElementById('theme-picker');
    if(!picker) return;
    var toggle = document.getElementById('theme-toggle');
    var options = document.getElementById('theme-options');
    toggle.addEventListener('click', function(e){ options.classList.toggle('d-none'); });
    options.addEventListener('click', function(e){
      var btn = e.target.closest('[data-color]');
      if(!btn) return;
      var color = btn.getAttribute('data-color');
      applyColor(color);
      localStorage.setItem('themeColor', color);
    });
    // close on outside click
    document.addEventListener('click', function(e){
      if(!picker.contains(e.target)) options.classList.add('d-none');
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', setupPicker);
  else setupPicker();
})();
