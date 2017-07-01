import Ember from 'ember';

export default Ember.Controller.extend({
  actions: {
    deleteActivo: function(id_activo){
      var self = this;
      this.get('store').findRecord('activo', id_activo, {backgroundReload: false}).then(function(activo){
        activo.destroyRecord();
        self.transitionToRoute('index');
      });
    }
  }
});
