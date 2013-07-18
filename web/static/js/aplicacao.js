function carregador() {
	
	var container, stats;

	var camera, scene, renderer, modelo;

	var mouseX = 0, mouseY = 0;

	var windowHalfX = window.innerWidth / 2;
	var windowHalfY = window.innerHeight / 2;
	var canvasWidth = 800;
	var canvasHeight = 600;

	var canvasHalfX = canvasWidth / 2;
	var canvasHalfY = canvasHeight / 2;

	var targetRotationY = 0;
	var targetRotationOnMouseDownY = 0;
	var mouseYOnMouseDown = 0;

	var soud;
	var marcadores = 1;

	function onWindowResize() {

		windowHalfX = window.innerWidth / 2;
		windowHalfY = window.innerHeight / 2;

		camera.aspect = window.innerWidth / window.innerHeight;
		camera.updateProjectionMatrix();

		renderer.setSize(window.innerWidth, window.innerHeight);
	}

	var Sound = function(sources, volume) {
		var audio = document.createElement('audio');

		for (var i = 0; i < sources.length; i++) {

			var source = document.createElement('source');
			source.src = sources[i];

			audio.appendChild(source);

		}

		this.play = function() {
			audio.play();

		}

		this.update = function(marcadores) {

			if (marcadores == 1) {

				audio.volume = 1;

			} else {

				audio.volume = 0;

			}

		}
	}
	function gira(sentido) {
		var gira = 0;
		if (sentido == 'direita') {
			gira += .2;
			marcadores = 1
		} else {
			marcadores = 0;
			gira += -.2;
		}
		//while(document.getElementById(sentido).mousedown){
		modelo.rotation.y += gira;
		if (modelo.rotation.y >= 360) {

			modelo.rotation.y = 0;
		} else if (modelo.rotation.y <= 0)
			modelo.rotation.y = 360;

		renderer.render(scene, camera);
		//}

	}

	if (doenca != 'False')
		iniciarTreino();
	init();
	animate();

	function init() {

		container = document.createElement('div');
		botaoEsquerda = document.getElementById('#esquerda');
		botaoDireita = $('#direita');
		document.getElementById('conteudo').appendChild(container);

		camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 2000);
		camera.position.z = 0;
		camera.position.y = 0;
		camera.rotation.x = 0;
		//camera.position.x = -50;
		// scene

		scene = new THREE.Scene();

		var ambient = new THREE.AmbientLight(0x101030);
		scene.add(ambient);

		var directionalLight = new THREE.DirectionalLight(0xffeedd);
		directionalLight.position.set(0, 0, 1).normalize();
		scene.add(directionalLight);

		// texture
		var texture = new THREE.Texture();

		var loader = new THREE.ImageLoader();
		loader.addEventListener('load', function(event) {

			texture.image = event.content;
			texture.needsUpdate = true;

		});
		//loader.load( 'textures/ash_uvgrid01.jpg' );

		// model

		var loader = new THREE.OBJLoader();
		loader.addEventListener('load', function(event) {

			modelo = event.content;
			//for ( var i = 0, l = object.children.length; i < l; i ++ ) {

			//object.children[ i ].material.map = texture;

			//}

			modelo.position.y = 0;
			modelo.position.z = -5;
			//modelo.rotation.x = 30;
			modelo.rotation.z = 0;

			//modelo = object;
			scene.add(modelo);
			camera.lookAt(modelo.position);
			//alert(modelo);

		});
		loader.load(media+'modelos/obj/CorpoHumanoHomem2.obj');

		//

		renderer = new THREE.WebGLRenderer();
		renderer.setSize(window.innerWidth, window.innerHeight);
		container.appendChild(renderer.domElement);

		window.addEventListener('resize', onWindowResize, false);

	}

	function animate() {

		requestAnimationFrame(animate);
		render();

	}

	function render() {

		renderer.render(scene, camera);
		sound.update(marcadores);

	}

	function iniciarTreino(doenca) {
		sound = new Sound([media+son], 100);
		isso = "aquilo";
		//sound1.position.copy(mesh1.position);
		alert('tocando')
		sound.play();
	}

}