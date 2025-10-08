const esbuild = require('esbuild');
const fs = require('fs');

async function bundleNostrTools() {
  try {
    console.log('🔄 Bundling nostr-tools...');
    
    const result = await esbuild.build({
      entryPoints: ['node_modules/nostr-tools/lib/index.js'],
      bundle: true,
      format: 'iife',
      globalName: 'nostrTools',
      outfile: 'nostr-tools-bundle.js',
      platform: 'browser',
      target: 'es2020',
      minify: false, // Keep readable for debugging
      sourcemap: false,
      external: [], // Bundle everything
    });
    
    console.log('✅ nostr-tools bundled successfully!');
    console.log('📁 Output: nostr-tools-bundle.js');
    
    // Verify the bundle was created
    if (fs.existsSync('nostr-tools-bundle.js')) {
      const stats = fs.statSync('nostr-tools-bundle.js');
      console.log(`📊 Bundle size: ${(stats.size / 1024).toFixed(2)} KB`);
    }
    
  } catch (error) {
    console.error('❌ Failed to bundle nostr-tools:', error);
    process.exit(1);
  }
}

bundleNostrTools();
