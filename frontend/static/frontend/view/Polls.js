Ext.define('MyApp.view.Polls', {
	extend: 'Ext.grid.Panel',
	id: 'polls',
	title: 'Polls',

	// store the grid is bound to
	store: 'Polls',
	autoLoad: true,

	// paging bar
	dockedItems: [{
		xtype: 'pagingtoolbar',
		dock: 'bottom',
		store: 'Polls',
		displayInfo: true
	}],

	// top toolbar
	tbar: [
		{text: 'delete', itemId: 'tbDelete'},
		{text: 'add', itemId: 'tbAdd'}
	],

	// select complete rows
	selType: 'rowmodel',

	plugins: [
		// enable row editor
		Ext.create('Ext.grid.plugin.RowEditing', {
			itemId: 'rowEditor',

			// on double-click
			clicksToEdit: 2
		}),

		// enable filterin in the column headers
		'gridfilters'
	],

	// configure columns
	columns: [
		{
			text: 'Question',
			dataIndex: 'question',
			flex: 1,
			filter: 'string',
			editor: {
				xtype: 'textfield',
				allowBlank: false
			},
			filter: {
				type: 'string'
			}
		}, {
			text: 'Publication-Date',
			dataIndex: 'pub_date',
			xtype: 'datecolumn',
			format:'l, d. F Y',
			width: 200,
			editor: {
				xtype: 'datefield',
				format: 'd.m.Y',
				allowBlank: false
			}
		}
	]
});
