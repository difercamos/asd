import Ember from 'ember';

export default Ember.Controller.extend({
  actions:{
    selectEstado: function(estado){
      this.set('estado', estado);
    },
    editActivo: function(id){
      var self = this;
      this.get('store').findRecord('activo', id).then(function(activo) {
        activo.set('nombre', self.get('model.nombre'));
        activo.set('descripcion', self.get('model.descripcion'));
        activo.set('tipo', self.get('model.tipo'));
        activo.set('serial', self.get('model.serial'));
        activo.set('numero_interno', self.get('model.numero_interno'));
        activo.set('peso', self.get('model.peso'));
        activo.set('alto', self.get('model.alto'));
        activo.set('ancho', self.get('model.ancho'));
        activo.set('largo', self.get('model.largo'));
        activo.set('valor_compra', self.get('model.valor_compra'));
        activo.set('fecha_compra', self.get('model.fecha_compra'));
        activo.set('estado', self.get('model.estado'));
        activo.set('color', self.get('model.color'));
        activo.save();
        self.transitionToRoute('index');
      });
    }
  }
});
