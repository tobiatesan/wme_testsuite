#include "scripts\const.inc"

global Scene;
global Keyboard;
global actor;


function rotate(sprite, deg) {
  var foo = 0;
  foo = foo + deg;
  if (sprite.Rotate==null) sprite.Rotate = 0;
  if (sprite.Rotatable!=true) sprite.Rotatable=true;
  sprite.Rotate = (sprite.Rotate+deg)%360;
}


function zoom(sprite, ratio) {
  if (sprite.Scalable!=true) {
  sprite.Scale = 100;
  sprite.Scalable=true;
  }
  sprite.Scale= (sprite.Scale)+ratio;
}


function sleepRoutine () {
	var i = 0;
	while (i < 10) {
		var j = 0;
		while (j < 10) {
			j = j + 1;
		}
		i = i + 1;
  }

}